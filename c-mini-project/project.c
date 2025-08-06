#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    int roll;
    char name[50];
    int present_days;
};

struct Student students[100];
int student_count = 0;

void addStudent() {
    printf("Enter Roll Number: ");
    scanf("%d", &students[student_count].roll);
    printf("Enter Name: ");
    getchar();  
    fgets(students[student_count].name, sizeof(students[student_count].name), stdin);
    students[student_count].name[strcspn(students[student_count].name, "\n")] = 0; 
    students[student_count].present_days = 0;
    student_count++;
    printf("Student added successfully!\n");
}

void markAttendance() {
    int roll, found = 0;
    printf("Enter Roll Number to mark present: ");
    scanf("%d", &roll);
    for(int i = 0; i < student_count; i++) {
        if(students[i].roll == roll) {
            students[i].present_days++;
            printf("Attendance marked for %s (Roll: %d)\n", students[i].name, roll);
            found = 1;
            break;
        }
    }
    if(!found) {
        printf("Student with Roll No %d not found.\n", roll);
    }
}

void viewAttendance() {
    printf("\n--- Attendance Sheet ---\n");
    printf("Roll\tName\t\tDays Present\n");
    for(int i = 0; i < student_count; i++) {
        printf("%d\t%-15s\t%d\n", students[i].roll, students[i].name, students[i].present_days);
    }
}

int main() {
    int choice;

    while(1) {
        printf("\n---- Attendance Management ----\n");
        printf("1. Add Student\n");
        printf("2. Mark Attendance\n");
        printf("3. View Attendance\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1: addStudent(); break;
            case 2: markAttendance(); break;
            case 3: viewAttendance(); break;
            case 4: printf("Exiting...\n"); return 0;
            default: printf("Invalid choice!\n");
        }
    }

    return 0;
}
