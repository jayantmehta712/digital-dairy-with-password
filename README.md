# Digital Diary with Password

A terminal-based personal diary application written in C. It protects diary entries with a password and stores entries locally with timestamps.

## Features

- Create a password on first run.
- Require password authentication on every launch.
- Add diary entries with date and time.
- View saved entries in chronological order.
- Change the password after verifying the current password.
- Store data locally in `diary.txt` and `pass.txt`.

## Repository Structure

```text
digital-dairy-with-password/
  digital_diary.c
  README.md
  .gitignore
  .gitattributes
```

## Compile

Use any standard C compiler:

```bash
gcc digital_diary.c -o digital_diary
```

On Windows with MinGW:

```bash
gcc digital_diary.c -o digital_diary.exe
```

## Run

Linux/macOS:

```bash
./digital_diary
```

Windows:

```bash
digital_diary.exe
```

## Data Files

| File | Purpose |
| --- | --- |
| `pass.txt` | Stores the diary password |
| `diary.txt` | Stores saved diary entries |

> Note: This is an educational project. The password is stored in plain text, so do not reuse a real personal password.

## Interview Talking Points

- Built a menu-driven C application with file handling.
- Used local persistence for passwords and diary entries.
- Added timestamped records using the C time library.
- Refactored the source into a portable `.c` file with clear compile instructions.
