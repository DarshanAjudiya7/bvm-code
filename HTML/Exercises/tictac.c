#include <stdio.h>
#include <stdlib.h>

// Function prototypes
void display_board(char board[3][3]);
int check_winner(char board[3][3]);
void make_move(char board[3][3], char player);

// Main function
int main() {
    char board[3][3] = { {'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'} };
    char current_player = 'X';
    int winner = 0;
    int moves = 0;

    printf("Welcome to Tic-Tac-Toe!\n");
    printf("Player 1: X | Player 2: O\n");

    while (1) {
        system("clear"); // Clear the console for better readability (use "cls" on Windows)
        display_board(board);

        // Player makes a move
        printf("\nPlayer %c's turn.\n", current_player);
        make_move(board, current_player);

        moves++;
        winner = check_winner(board);

        // Check if there is a winner or a draw
        if (winner) {
            system("clear");
            display_board(board);
            printf("\nPlayer %c wins! Congratulations!\n", current_player);
            break;
        } else if (moves == 9) {
            system("clear");
            display_board(board);
            printf("\nIt's a draw!\n");
            break;
        }

        // Switch player
        current_player = (current_player == 'X') ? 'O' : 'X';
    }

    return 0;
}

// Function to display the Tic-Tac-Toe board
void display_board(char board[3][3]) {
    printf("\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf(" %c ", board[i][j]);
            if (j < 2) printf("|");
        }
        printf("\n");
        if (i < 2) printf("---|---|---\n");
    }
}

// Function to check if there is a winner
int check_winner(char board[3][3]) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) return 1;
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) return 1;
    }

    // Check diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) return 1;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) return 1;

    return 0;
}

// Function to make a move on the board
void make_move(char board[3][3], char player) {
    int choice;
    int row, col;
    while (1) {
        printf("Enter the number of the cell where you want to place your mark: ");
        scanf("%d", &choice);

        if (choice < 1 || choice > 9) {
            printf("Invalid input! Please choose a number between 1 and 9.\n");
            continue;
        }

        // Map the choice to the board's row and column
        row = (choice - 1) / 3;
        col = (choice - 1) % 3;

        // Check if the cell is already occupied
        if (board[row][col] == 'X' || board[row][col] == 'O') {
            printf("Cell already occupied! Choose another cell.\n");
        } else {
            board[row][col] = player;
            break;
        }
    }
}
