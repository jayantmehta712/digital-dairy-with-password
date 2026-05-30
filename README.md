# Digital Diary with Password

A terminal-based personal diary application written in C that protects your entries with a password. All diary entries are stored locally with timestamps, and access is gated behind a password authentication system.

---

## Repository Structure

```
digital-dairy-with-password/
├── digiTAL diary with password                          # Main C source file (Digital Diary)
├── bakery_management by jayant in py.py                 # Bakery management system (Python)
├── credit_card_fraud_detection using py and ml.py       # Credit card fraud detection (Python/ML)
├── customer_churn_prediction by jay using ml and py.py  # Customer churn prediction (Python/ML)
├── .gitignore
└── .gitattributes
```

---

## Features

- **Password Protection** — Set a password on first run; all subsequent access requires authentication
- **Add Entries** — Write diary entries (up to 500 characters) saved with a date-time timestamp
- **View Entries** — Read all previously saved entries in chronological order
- **Change Password** — Update your password securely after verifying the current one
- **Persistent Storage** — Entries and password are saved to local files (`diary.txt`, `pass.txt`)

---

## Requirements

- GCC or any standard C compiler
- Unix/Linux environment (requires `<unistd.h>`)

---

## Getting Started

### Compile

```bash
gcc "digiTAL diary with password" -o digital_diary
```

### Run

```bash
./digital_diary
```

On first launch, you will be prompted to create a password. Subsequent runs will require that password before granting access.

---

## Usage

```
--- Digital Diary Menu ---
1. Add Entry
2. View Entries
3. Change Password
4. Exit
```

- **Add Entry** — Type your diary entry (up to 500 characters). It is saved with a timestamp in `YYYY-MM-DD HH:MM:SS` format.
- **View Entries** — Displays all past entries along with their timestamps.
- **Change Password** — Verifies your current password before allowing a new one to be set.
- **Exit** — Closes the application.

---

## Data Files

| File        | Purpose                          |
|-------------|----------------------------------|
| `pass.txt`  | Stores the diary password        |
| `diary.txt` | Stores all diary entries         |

> **Note:** The password is stored in plain text in `pass.txt`. Avoid reusing sensitive or personal passwords.

---

## Other Projects in This Repository

| File | Description |
|------|-------------|
| `bakery_management by jayant in py.py` | A bakery management system built in Python |
| `credit_card_fraud_detection using py and ml.py` | Credit card fraud detection using Python and Machine Learning |
| `customer_churn_prediction by jay using ml and py.py` | Customer churn prediction using Python and Machine Learning |

---

## Author

**Jayant Mehta**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jayant-mehta-b2752a302/)

---

## License

This project is open-source and available for personal and educational use.
