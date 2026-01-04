
import argparse
import json
import os
from datetime import datetime

CHALLANS_FILE = "challans.json"

def initialize_storage():
    if not os.path.exists(CHALLANS_FILE):
        with open(CHALLANS_FILE, "w") as f:
            json.dump([], f)

def add_challan(args):
    """Adds a new challan."""
    initialize_storage()
    with open(CHALLANS_FILE, "r+") as f:
        challans = json.load(f)
        challan = {
            "id": len(challans) + 1,
            "vehicle_number": args.vehicle_number,
            "violation": args.violation,
            "fine_amount": args.fine_amount,
            "date": datetime.now().isoformat(),
            "paid": False,
        }
        challans.append(challan)
        f.seek(0)
        json.dump(challans, f, indent=4)
    print(f"Challan added successfully with ID: {challan['id']}")

def view_challans(args):
    """Views all challans or a specific one by ID."""
    initialize_storage()
    with open(CHALLANS_FILE, "r") as f:
        challans = json.load(f)
        if args.id:
            challan = next((c for c in challans if c["id"] == args.id), None)
            if challan:
                print(json.dumps(challan, indent=4))
            else:
                print("Challan not found.")
        else:
            print(json.dumps(challans, indent=4))

def pay_challan(args):
    """Marks a challan as paid."""
    initialize_storage()
    with open(CHALLANS_FILE, "r+") as f:
        challans = json.load(f)
        challan = next((c for c in challans if c["id"] == args.id), None)
        if challan:
            challan["paid"] = True
            f.seek(0)
            f.truncate()
            json.dump(challans, f, indent=4)
            print(f"Challan {args.id} marked as paid.")
        else:
            print("Challan not found.")

def main():
    parser = argparse.ArgumentParser(description="Traffic Challan Management System")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add challan command
    add_parser = subparsers.add_parser("add", help="Add a new challan")
    add_parser.add_argument("vehicle_number", help="Vehicle number")
    add_parser.add_argument("violation", help="Violation description")
    add_parser.add_argument("fine_amount", type=int, help="Fine amount")
    add_parser.set_defaults(func=add_challan)

    # View challans command
    view_parser = subparsers.add_parser("view", help="View challans")
    view_parser.add_argument("--id", type=int, help="View a specific challan by ID")
    view_parser.set_defaults(func=view_challans)

    # Pay challan command
    pay_parser = subparsers.add_parser("pay", help="Mark a challan as paid")
    pay_parser.add_argument("id", type=int, help="The ID of the challan to mark as paid")
    pay_parser.set_defaults(func=pay_challan)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
