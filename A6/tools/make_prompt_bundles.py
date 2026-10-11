"""Builds the exact prompt files that team members paste into a free LLM.

Each prompt file = instruction text + the verbatim source excerpts it refers to,
so the saved prompt is exactly what the model received.
Run from the A6 folder:  python tools/make_prompt_bundles.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODE = ROOT / "Part1" / "code"

def excerpt(rel, start=None, end=None):
    lines = (CODE / rel).read_text(encoding="utf-8").splitlines()
    s = start or 1
    e = end or len(lines)
    body = "\n".join(f"{i:4d} {lines[i-1]}" for i in range(s, e + 1))
    return f"----- FILE: Part1/code/{rel} (lines {s}-{e}) -----\n{body}\n"

CONTEXT = (
    "Context: Sarathi is an open-source Node.js/Express/TypeScript ride-sharing (driver-hire) backend "
    "(https://github.com/AkhilMM2000/sarathi-backend, commit c8766f4). It uses MongoDB/Mongoose, "
    "tsyringe dependency injection, Socket.IO, Upstash Redis, Stripe and the Google Distance Matrix API. "
    "Line numbers are shown at the left of every source line.\n"
)

PROMPTS = {
    "Dilip_Kumar_Reddy_prompt_01.txt": (
        "Pattern discovery",
        CONTEXT +
        "Task: Identify the design patterns that are ACTUALLY implemented in the code below "
        "(GoF, GRASP, enterprise/architectural patterns and framework idioms). The code covers the rider, "
        "driver, trip (booking), payment, driver matching, location and notification areas.\n"
        "For each pattern give: (1) exact pattern name and category, (2) a meaningful instance name, "
        "(3) every participant role mapped to the actual class/interface/function, (4) file path and line range "
        "of each participant, (5) the code interactions that prove it. "
        "Then list candidate patterns that are NOT really present (for example because only one implementation "
        "exists or roles are missing) and explain why. Do not invent classes that are not in the code.\n\n",
        [
            ("src/domain/repositories/IBaseRepository.ts",),
            ("src/infrastructure/database/BaseRepository.ts",),
            ("src/domain/repositories/IBookingrepository.ts", 17, 62),
            ("src/infrastructure/database/MongoBookingRepository.ts", 1, 24),
            ("src/application/services/NotificationService.ts",),
            ("src/infrastructure/services/SocketNotification.ts",),
            ("src/infrastructure/socket/socket.ts", 1, 20),
            ("src/infrastructure/socket/socket.ts", 178, 184),
            ("src/infrastructure/socket/SocketNotification.ts", 13, 40),
            ("src/application/services/FareCalculatorService.ts",),
            ("src/infrastructure/services/FareCalculatorService.ts",),
            ("src/application/use_cases/User/BookDriver.ts", 27, 60),
            ("src/application/use_cases/Driver/AcceptBooking.ts",),
            ("src/domain/services/IStripeService.ts",),
            ("src/infrastructure/services/StripeService.ts", 1, 50),
            ("src/middleware/authMiddleware.ts",),
            ("src/middleware/checkBlocked.ts", 10, 30),
            ("src/infrastructure/utils/catchAsync.ts",),
            ("src/presentation/routes/BookingRoute.ts",),
            ("src/infrastructure/config/container.ts", 44, 101),
        ],
    ),
    "Sai_Sameer_prompt_01.txt": (
        "Evolution CH01 (new driver status)",
        CONTEXT +
        "New requirement (Agile change CH01 - new driver status): an admin must be able to temporarily SUSPEND an "
        "approved driver (reason required) and later REINSTATE the driver. A suspended driver must not receive ride "
        "requests and must not be able to accept a booking. Today a driver status is only pending/approved/rejected and "
        "the admin can move a driver from any status to any status.\n"
        "Questions: (1) Which code smells in the current driver-status handling make this change risky? "
        "(2) Which design pattern(s) would you introduce and why? Name every participant. "
        "(3) Which existing patterns in this code are preserved, modified, extended, replaced or removed by your design? "
        "(4) Show the TypeScript changes needed in the files below.\n\n",
        [
            ("src/domain/models/Driver.ts",),
            ("src/infrastructure/database/modals/Driverschema.ts", 28, 45),
            ("src/domain/repositories/IDriverepository.ts",),
            ("src/infrastructure/database/MongodriverRepository.ts", 89, 102),
            ("src/infrastructure/database/MongodriverRepository.ts", 243, 287),
            ("src/application/use_cases/Admin/AdminChangeDriverStatus.ts",),
            ("src/application/use_cases/Driver/AcceptBooking.ts",),
            ("src/application/services/NotificationService.ts",),
        ],
    ),
    "M_Kumar_prompt_01.txt": (
        "Evolution CH02 (ride cancellation)",
        CONTEXT +
        "New requirement (Agile change CH02 - ride cancellation): both the rider and the assigned driver can cancel a "
        "ride. Only PENDING or CONFIRMED rides can be cancelled; COMPLETED, CANCELLED, REJECTED or EXPIRED rides must "
        "be refused. A rider cancelling a CONFIRMED ride after 9:00 PM IST on the day before the ride pays a late "
        "cancellation fee of 10% of the estimated fare (minimum Rs 50); all other rider cancellations are free. A driver "
        "cancellation is free for the rider and the rider must be notified. Only the rider or driver of that booking "
        "may cancel it.\n"
        "Questions: (1) Which code smells or defects in the current cancellation and status-update code make this "
        "change risky? (2) Which design pattern(s) would you introduce and why? Name every participant. "
        "(3) Which existing patterns are preserved, modified, extended, replaced or removed? "
        "(4) Show the TypeScript changes needed in the files below.\n\n",
        [
            ("src/domain/models/Booking.ts",),
            ("src/application/use_cases/User/CancelBooking.ts",),
            ("src/application/use_cases/Driver/UpdateBookingstatus.ts",),
            ("src/application/use_cases/Driver/AcceptBooking.ts",),
            ("src/infrastructure/services/CronScheduler.ts",),
            ("src/presentation/controllers/BookingController.ts", 193, 204),
            ("src/application/services/NotificationService.ts",),
        ],
    ),
    "K_Harish_prompt_01.txt": (
        "Evolution CH03 (ride types and dynamic pricing)",
        CONTEXT +
        "New requirement (Agile change CH03 - multiple ride types and dynamic pricing): besides ONE_WAY (Rs 10/km, "
        "minimum Rs 450) and ROUND_TRIP/RANGE_OF_DATES (Rs 1000/day) add HOURLY (Rs 200/hour, minimum 4 hours) and "
        "OUTSTATION (Rs 12/km plus Rs 300 driver allowance per day). Add dynamic pricing: +25% when the ride starts in "
        "peak hours (08:00-10:59 or 17:00-20:59 IST) and +20% when fewer than 3 drivers are available near the pickup. "
        "Adding a new ride type or pricing rule should not require editing existing fare code.\n"
        "Questions: (1) Which code smells in the current fare code make this change risky? "
        "(2) Which design pattern(s) would you introduce and why? Name every participant. "
        "(3) Which existing patterns are preserved, modified, extended, replaced or removed? "
        "(4) Show the TypeScript changes needed in the files below.\n\n",
        [
            ("src/domain/models/Booking.ts",),
            ("src/application/services/FareCalculatorService.ts",),
            ("src/infrastructure/services/FareCalculatorService.ts",),
            ("src/application/use_cases/User/GetEstimatedFare.ts",),
            ("src/application/use_cases/User/BookDriver.ts", 27, 100),
            ("src/application/use_cases/Driver/UpdateBookingstatus.ts", 26, 64),
        ],
    ),
}

CROSS = {
    "Sai_Sameer_prompt_02.txt": (
        "Cross-language analysis (Observer)",
        "Implement the following small problem with the Observer pattern in Java, Python, JavaScript and C++, with "
        "identical behaviour in all four languages, then compare the four implementations (participant structure, "
        "interfaces vs duck typing, inheritance vs composition, memory/ownership, static vs dynamic typing, "
        "lines of code and complexity).\n\n" + (ROOT / "Part3" / "test-cases" / "observer_spec.md").as_posix(),
    ),
    "M_Kumar_prompt_02.txt": (
        "Cross-language analysis (State)",
        "Implement the following small problem with the State pattern in Java, Python, JavaScript and C++, with "
        "identical behaviour in all four languages, then compare the four implementations (participant structure, "
        "interfaces vs duck typing, inheritance vs composition, memory/ownership, static vs dynamic typing, "
        "lines of code and complexity).\n\n" + (ROOT / "Part3" / "test-cases" / "state_spec.md").as_posix(),
    ),
    "K_Harish_prompt_02.txt": (
        "Cross-language analysis (Strategy)",
        "Implement the following small problem with the Strategy pattern in Java, Python, JavaScript and C++, with "
        "identical behaviour in all four languages, then compare the four implementations (participant structure, "
        "interfaces vs duck typing, inheritance vs composition, memory/ownership, static vs dynamic typing, "
        "lines of code and complexity).\n\n" + (ROOT / "Part3" / "test-cases" / "strategy_spec.md").as_posix(),
    ),
}

def whole(rel):
    return f"----- FILE: {rel} -----\n" + (ROOT / rel).read_text(encoding="utf-8") + "\n"


# Prompts whose input is a team dataset file rather than application source.
DATASET = {
    "S_Leela_Shankar_prompt_01.txt": (
        "Pattern discovery (dataset audit)",
        "Below are two CSV files from a design-pattern case study of a Node.js/Express ride-sharing backend. "
        "patterns.csv has one row per confirmed pattern instance in the original code (participant roles mapped to "
        "classes/functions, file:line locations and evidence). pattern_counts.csv summarises them.\n"
        "Tasks: (1) Check that every count in pattern_counts.csv for 'Original code' matches the rows of patterns.csv. "
        "(2) For each row, say whether the participant roles are complete and consistent with the named pattern "
        "(for example: does an Adapter row name Target, Adapter and Adaptee? does an Observer row name subject, "
        "subscription and notification?). (3) Point out any row whose pattern name or category looks wrong, or two rows "
        "that should be one instance, and explain why. Do not assume facts that are not in the files.\n\n",
        ["data/patterns.csv", "data/pattern_counts.csv"],
    ),
    "S_Leela_Shankar_prompt_02.txt": (
        "Cross-language analysis (metrics)",
        "Below is cross_language.csv from a case study that implemented the same Strategy, State and Observer problems in "
        "Java, Python, JavaScript and C++ with identical test fixtures. source_loc = non-blank non-comment lines of the "
        "production file (lizard), max_function_cc = maximum cyclomatic complexity, median_process_ms = median wall time "
        "of 5 complete test processes after 1 warm-up (Java/Python/JS on Windows 11, C++ inside a Linux Docker container, "
        "container start-up excluded).\n"
        "Tasks: (1) Explain the main differences in LOC, complexity and time between the languages for each pattern. "
        "(2) Which differences come from the language (typing, dispatch, memory management, runtime start-up) and which "
        "from implementation choices? (3) List threats to validity of these measurements. (4) Is it fair to conclude that "
        "one language implements these patterns 'better'? Justify.\n\n",
        ["data/cross_language.csv"],
    ),
}


def main():
    out = ROOT / "prompts"
    out.mkdir(exist_ok=True)
    for name, (part, text, files) in DATASET.items():
        body = text + "\n".join(whole(f) for f in files)
        (out / name).write_text(body, encoding="utf-8", newline="\n")
        print(f"{name}: {part}, {len(body)} chars")
    for name, (part, text, files) in PROMPTS.items():
        body = text + "\n".join(excerpt(*f) for f in files)
        (out / name).write_text(body, encoding="utf-8", newline="\n")
        print(f"{name}: {part}, {len(body)} chars")
    for name, (part, text) in CROSS.items():
        head, spec_path = text.rsplit("\n\n", 1)
        spec = Path(spec_path).read_text(encoding="utf-8")
        body = head + "\n\n" + spec
        (out / name).write_text(body, encoding="utf-8", newline="\n")
        print(f"{name}: {part}, {len(body)} chars")

if __name__ == "__main__":
    main()
