#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_ENTRY 500
#define MAX_PASSWORD 100
#define PASSFILE "pass.txt"
#define DIARYFILE "diary.txt"

static void trim_newline(char *text) {
    text[strcspn(text, "\n")] = '\0';
}

static int file_exists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        return 0;
    }
    fclose(file);
    return 1;
}

static void read_line(char *buffer, size_t size) {
    if (fgets(buffer, size, stdin) == NULL) {
        buffer[0] = '\0';
        return;
    }
    trim_newline(buffer);
}

static void set_password(void) {
    char password[MAX_PASSWORD];
    char confirm[MAX_PASSWORD];

    printf("Create password: ");
    read_line(password, sizeof(password));

    printf("Confirm password: ");
    read_line(confirm, sizeof(confirm));

    if (strcmp(password, confirm) != 0) {
        printf("Passwords do not match. Try again.\n");
        set_password();
        return;
    }

    FILE *file = fopen(PASSFILE, "w");
    if (file == NULL) {
        printf("Unable to save password.\n");
        return;
    }

    fprintf(file, "%s", password);
    fclose(file);
    printf("Password set successfully.\n");
}

static int check_password(void) {
    char saved[MAX_PASSWORD];
    char input[MAX_PASSWORD];

    FILE *file = fopen(PASSFILE, "r");
    if (file == NULL) {
        return 0;
    }

    if (fgets(saved, sizeof(saved), file) == NULL) {
        fclose(file);
        return 0;
    }
    fclose(file);
    trim_newline(saved);

    printf("Enter password: ");
    read_line(input, sizeof(input));

    return strcmp(saved, input) == 0;
}

static void add_entry(void) {
    char entry[MAX_ENTRY];
    char timestamp[32];
    time_t now = time(NULL);
    struct tm *local_time = localtime(&now);

    printf("Write your entry (max %d characters):\n", MAX_ENTRY - 1);
    read_line(entry, sizeof(entry));

    strftime(timestamp, sizeof(timestamp), "%Y-%m-%d %H:%M:%S", local_time);

    FILE *file = fopen(DIARYFILE, "a");
    if (file == NULL) {
        printf("Unable to save diary entry.\n");
        return;
    }

    fprintf(file, "[%s]\n%s\n\n", timestamp, entry);
    fclose(file);
    printf("Entry saved.\n");
}

static void view_entries(void) {
    char line[600];
    FILE *file = fopen(DIARYFILE, "r");

    if (file == NULL) {
        printf("No entries found.\n");
        return;
    }

    printf("\n--- Diary Entries ---\n");
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }
    fclose(file);
}

static void change_password(void) {
    if (!check_password()) {
        printf("Incorrect current password.\n");
        return;
    }
    set_password();
}

int main(void) {
    int choice = 0;

    if (!file_exists(PASSFILE)) {
        printf("No password set. Please create one.\n");
        set_password();
    }

    if (!check_password()) {
        printf("Access denied.\n");
        return 1;
    }

    do {
        printf("\n--- Digital Diary Menu ---\n");
        printf("1. Add Entry\n");
        printf("2. View Entries\n");
        printf("3. Change Password\n");
        printf("4. Exit\n");
        printf("Your choice: ");

        if (scanf("%d", &choice) != 1) {
            printf("Invalid input.\n");
            return 1;
        }
        getchar();

        switch (choice) {
            case 1:
                add_entry();
                break;
            case 2:
                view_entries();
                break;
            case 3:
                change_password();
                break;
            case 4:
                printf("Goodbye.\n");
                break;
            default:
                printf("Invalid choice.\n");
        }
    } while (choice != 4);

    return 0;
}
