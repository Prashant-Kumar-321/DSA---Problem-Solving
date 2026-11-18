/**
 * https://cs50.harvard.edu/x/psets/3/tideman/ * 
*/

#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
int victory_strength(pair p); 
bool is_there_cycle(bool visited[], int src); 

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    for (int i = 0; i < candidate_count; ++i)
    {
        for (int j = 0; j < candidate_count; ++j)
        {
            printf("%i ", preferences[i][j]); 
        }
        printf("\n"); 
    }

    add_pairs();

    for (int i = 0; i < pair_count; ++i){
        printf("Winner: %s\n", candidates[pairs[i].winner]); 
        printf("Loser: %s\n", candidates[pairs[i].loser]); 
        printf("\n"); 
    }

    sort_pairs();
    lock_pairs();

    for (int i = 0; i < candidate_count; ++i)
    {
        for (int j = 0; j < candidate_count; ++j)
        {
            printf("%i ", locked[i][j]); 
        }
        printf("\n");
    }

    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // Validate name is oen of the candidates
    for (int i = 0; i < candidate_count; ++i)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i; 
            return true; 
        }
    }

    // No candidate is matched for the name
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; ++i)
    {
        for (int j = i + 1; j < candidate_count; ++j)
        {
            preferences[ranks[i]][ranks[j]]++; 
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; ++i)
    {
        for (int j = i + 1; j < candidate_count; ++j)
        {
            // Pair of candidate not added if tied
            if (preferences[i][j] == preferences[j][i]) 
            {
                continue; 
            }

            // Added pairs of candidate only when one is prefered over other
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i; 
                pairs[pair_count].loser = j; 
            }
            else 
            {
                pairs[pair_count].winner = j; 
                pairs[pair_count].loser = i; 
            }

            pair_count += 1; 
        }
    }
    return;
}

int victory_strength(pair p)
{
    printf("%i, ", preferences[p.winner][p.loser] - preferences[p.loser][p.winner]); 
    return preferences[p.winner][p.loser] - preferences[p.loser][p.winner]; 
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // Using Optimize Bubble Sort to sort the pairs of candidates
    for (int i = 0; i < pair_count; ++i)
    {
        bool swapped = false; 
        
        for (int j = i; j < pair_count - i - 1; ++j)
        {
            if (victory_strength(pairs[j]) < victory_strength(pairs[j + 1]))
            {
                // Swap Adjacent Pairs
                pair temp = {.winner = pairs[j + 1].winner, .loser = pairs[j + 1].loser}; 
                pairs[j + 1].winner = pairs[j].winner; 
                pairs[j +  1].loser = pairs[j].loser; 

                pairs[j].winner =  temp.winner; 
                pairs[j].loser = temp.loser; 

                swapped = true; 
            }
        }

        // Optimization Code
        // if No any swapped occured break the loop as pairs are already sorted.
        if (!swapped)
        {
            break; 
        }
    }
    return;
}

// Detect if there is cycle from current source
bool is_there_cycle(bool visited[], int node)
{
    if (visited[node] == true)
    {
        return true; 
    }

    // locked [][] = graph
    // visited array track node visited
    visited[node] = true;

    for (int i = 0; i < candidate_count; ++i)
    {
        if (locked[node][i] == true)
        {
            return is_there_cycle(visited, i); 
        }
    }

    return false; 
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // Iterate over pairs and locks each pair if it does not lead to cycle
    for (int i = 0; i < pair_count; ++i)
    {
        // Adding a edge in the graph
        locked[pairs[i].winner][pairs[i].loser] = true; 

        // Create a visited array to track the visited candidates
        bool visited[MAX] = {false}; 
        visited[pairs[i].winner] = true; 
        if (is_there_cycle(visited, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = false; 
        }
    }
    
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    return;
}

