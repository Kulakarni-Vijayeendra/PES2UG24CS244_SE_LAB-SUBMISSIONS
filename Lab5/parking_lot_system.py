"""Parking lot management system with improved quality and security."""

import hashlib
import secrets

parking_slots = {
    "P01": {
        "plate": "KA01AB1234",
        "hours": 2,
        "rate": 20.0,
        "is_occupied": True,
    },
    "P02": {
        "plate": "",
        "hours": 0,
        "rate": 20.0,
        "is_occupied": False,
    },
    "P03": {
        "plate": "MH02EF9012",
        "hours": 4,
        "rate": 30.0,
        "is_occupied": True,
    },
}

total_collections = 0.0


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle and record the parking charge."""
    global total_collections

    if entry_logs is None:
        entry_logs = []

    if slot_id not in parking_slots or parking_slots[slot_id]["is_occupied"]:
        return False
    if not isinstance(hours_booked, int) or hours_booked < 1:
        raise ValueError("Booked hours must be a positive integer")
    if not isinstance(plate_no, str) or not plate_no.strip():
        raise ValueError("Vehicle plate number cannot be empty")

    slot = parking_slots[slot_id]
    slot["plate"] = plate_no.strip()
    slot["hours"] = hours_booked
    slot["is_occupied"] = True
    total_collections += slot["rate"] * hours_booked
    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} for "
        f"{hours_booked} hours"
    )
    return True


def release_slot(slot_id):
    """Release a parking slot if it exists."""
    if slot_id not in parking_slots:
        return False

    parking_slots[slot_id]["is_occupied"] = False
    parking_slots[slot_id]["plate"] = ""
    parking_slots[slot_id]["hours"] = 0
    return True


def check_slot_availability(slot_id):
    """Return whether a valid parking slot is vacant."""
    slot = parking_slots.get(slot_id)
    return slot is not None and not slot["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier=1.0):
    """Calculate the fee using a validated surge multiplier."""
    if slot_id not in parking_slots:
        raise ValueError("Unknown parking slot")
    if isinstance(surge_multiplier, bool) or not isinstance(
        surge_multiplier, (int, float)
    ):
        raise ValueError("Surge multiplier must be numeric")
    if not 1.0 <= surge_multiplier <= 5.0:
        raise ValueError("Surge multiplier must be between 1 and 5")

    base_rate = parking_slots[slot_id]["rate"]
    return base_rate * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Return a SHA-256 hash of a vehicle plate number."""
    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def generate_ticket_pin():
    """Generate a random four-digit ticket PIN."""
    return secrets.randbelow(9000) + 1000


def export_parking_manifest(filename="parking_manifest.txt"):
    """Export parking slot details to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(parking_slots))
    print(f"Parking manifest exported to: {filename}")


def get_available_summary(slots):
    """Count vacant parking slots."""
    return sum(
        1 for details in slots.values()
        if not details["is_occupied"]
    )


def main():
    """Demonstrate the parking lot system."""
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")

    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.50))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())

    export_parking_manifest()
    print("Vacant slots:", get_available_summary(parking_slots))


if __name__ == "__main__":
    main()
