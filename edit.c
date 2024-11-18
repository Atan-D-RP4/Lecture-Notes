int min(int a, int b, int c) {
    return a < b ? (a < c ? a : c) : (b < c ? b : c);
}

int minDistance(char *s1, char *s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);

    // Create a matrix to store the distances
    int matrix[len1 + 1][len2 + 1];

    // Initialize the matrix
    for (int i = 0; i <= len1; ++i)
        matrix[i][0] = i;
    
    for (int i = 0; i <= len2; ++i)
        matrix[0][i] = i;

    // Fill in the matrix
    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            if (s1[i - 1] == s2[j - 1])
                matrix[i][j] = matrix[i - 1][j - 1];
            else
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]);
        }
    }

    // The bottom-right cell of the matrix contains the Levenshtein distance
    return matrix[len1][len2];
}