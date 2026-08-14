def find_motif_locations(s, t):
    """
    Finds all 1-based starting locations of substring t in string s.
    Problem ID: SUBS (Rosalind)
    """
    locations = []
    len_s = len(s)
    len_t = len(t)
    
    # Loop through string s to check every possible starting position
    for i in range(len_s - len_t + 1):
        if s[i:i + len_t] == t:
            # Add 1 because Rosalind uses 1-based indexing
            locations.append(i + 1)
            
    return locations

if __name__ == "__main__":
    # Sample Dataset from Rosalind
    s = "GATATATGCATATACTT"
    t = "ATAT"
    
    result = find_motif_locations(s, t)
    # Print locations separated by space as required by Rosalind
    print("Sample Output:", *result)  # Output: 2 4 10
