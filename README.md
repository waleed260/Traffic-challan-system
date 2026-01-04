# Traffic Challan Management System

This is a simple command-line application to manage traffic challans.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/traffic-challan-system.git
    cd traffic-challan-system
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The application is run from the command line using `python main.py`.

### Add a new challan

```bash
python main.py add <vehicle_number> <violation> <fine_amount>
```

**Example:**

```bash
python main.py add "MH12AB1234" "Speeding" 500
```

### View all challans

```bash
python main.py view
```

### View a specific challan

```bash
python main.py view --id <challan_id>
```

**Example:**

```bash
python main.py view --id 1
```

### Mark a challan as paid

```bash
python main.py pay <challan_id>
```

**Example:**

```bash
python main.py pay 1
```
