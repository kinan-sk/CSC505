# ATM State Machine Sequence Printer
# This script documents the execution flow of the ATM State Machine Diagram
# by printing the states, events, guards, and actions in sequence for key
# operations depicted in my UML diagram.

import time

def print_separator(title):
    """Prints a descriptive separator for each operational sequence."""
    print("\n" + "=" * 80)
    print(f"| {title:^76} |")
    print("=" * 80)

def print_step(step_number, current_state, transition_event, transition_action, next_state):
    """Prints a formatted step showing the state change."""
    print(f"\n[{step_number}] CURRENT STATE: {current_state}")
    print(f"    EVENT TRIGGERED: {transition_event}")
    print(f"    ACTION / GUARD: {transition_action}")
    print(f"    -> NEXT STATE: {next_state}")

# --- OPERATION 1: SUCCESSFUL WITHDRAWAL SEQUENCE ---

def successful_withdrawal_sequence():
    """Prints the full sequence for a customer successfully withdrawing money."""
    print_separator("OPERATION 1: SUCCESSFUL WITHDRAWAL SEQUENCE")
    step = 1

    # State: IDLE -> WAITING FOR CARD
    print(f"[{step}] START: Initial Node -> WAITING FOR CARD")
    print("    (Entry Action of WAITING FOR CARD: initialize system status; turn on screen)")
    step += 1

    # State: WAITING FOR CARD -> WAITING FOR PIN
    print_step(step,
               "WAITING FOR CARD",
               "Insert Card",
               "/ reset attempt counter; prompt for PIN",
               "WAITING FOR PIN (Entry Action: reset PIN input buffer; start PIN entry timer)")
    step += 1

    # State: WAITING FOR PIN -> AUTHENTICATED
    print_step(step,
               "WAITING FOR PIN",
               "Enter PIN [PIN is correct]",
               "/ display service menu",
               "AUTHENTICATED (Entry Action: log successful authentication; reset timeout timer)")
    step += 1

    # State: AUTHENTICATED -> PROCESSING WITHDRAWAL
    print_step(step,
               "AUTHENTICATED",
               "Select Withdrawal",
               "/ prompt for amount",
               "PROCESSING WITHDRAWAL (Entry Action: prompt for amount; start transaction timer)")
    step += 1

    # State: PROCESSING WITHDRAWAL -> TRANSACTION SUCCESS
    # Assuming user requests $100 and has $500 balance, within $200 limit
    print_step(step,
               "PROCESSING WITHDRAWAL",
               "Enter Amount [$100 <= $500 balance AND $100 <= $200 limit]",
               "/ dispense cash; debit account; print receipt",
               "TRANSACTION SUCCESS (Entry Action: disable keypad)")
    step += 1

    # State: TRANSACTION SUCCESS -> AUTHENTICATED (User chooses to continue)
    print_step(step,
               "TRANSACTION SUCCESS",
               "OK",
               "/ prompt for next transaction",
               "AUTHENTICATED (Entry Action: log successful authentication; reset timeout timer)")
    step += 1

    # State: AUTHENTICATED -> EJECTING CARD (User chooses to exit)
    print_step(step,
               "AUTHENTICATED",
               "Select Exit",
               "/ eject card",
               "EJECTING CARD (Entry Action: eject card; print transaction receipt)")
    step += 1

    # State: EJECTING CARD -> FINAL NODE
    print_step(step,
               "EJECTING CARD",
               "Timeout / Card Removed",
               "/ log session terminated",
               "FINAL NODE")

# --- OPERATION 2: SUCCESSFUL BALANCE CHECK SEQUENCE ---

def successful_balance_check_sequence():
    """Prints the full sequence for a customer successfully checking their balance and exiting."""
    print_separator("OPERATION 2: SUCCESSFUL BALANCE CHECK SEQUENCE")
    step = 1

    # Steps 1-3 are identical to the start of the withdrawal sequence (Initial Node to AUTHENTICATED)
    print("... (Initial steps 1-3 are identical: IDLE -> WAITING FOR CARD -> WAITING FOR PIN -> AUTHENTICATED) ...")
    step = 4 # Start from the AUTHENTICATED state

    # State: AUTHENTICATED -> DISPLAYING BALANCE
    print_step(step,
               "AUTHENTICATED",
               "Select Balance",
               "/ retrieve account balance",
               "DISPLAYING BALANCE (Entry Action: retrieve account balance)")
    step += 1

    # State: DISPLAYING BALANCE -> EJECTING CARD (User chooses to exit immediately)
    print_step(step,
               "DISPLAYING BALANCE",
               "Select Exit",
               "/ eject card; print receipt",
               "EJECTING CARD (Entry Action: eject card; print transaction receipt)")
    step += 1

    # State: EJECTING CARD -> FINAL NODE
    print_step(step,
               "EJECTING CARD",
               "Timeout / Card Removed",
               "/ log session terminated",
               "FINAL NODE")

# --- OPERATION 3: FAILED AUTHENTICATION SEQUENCE (CARD TRAPPED) ---

def failed_authentication_sequence():
    """Prints the full sequence for a customer failing authentication and having their card trapped."""
    print_separator("OPERATION 3: FAILED AUTHENTICATION (CARD TRAPPED) SEQUENCE")
    step = 1

    # State: IDLE -> WAITING FOR CARD
    print(f"[{step}] START: Initial Node -> WAITING FOR CARD")
    print("    (Entry Action of WAITING FOR CARD: initialize system status; turn on screen)")
    step += 1

    # State: WAITING FOR CARD -> WAITING FOR PIN
    print_step(step,
               "WAITING FOR CARD",
               "Insert Card",
               "/ reset attempt counter; prompt for PIN",
               "WAITING FOR PIN (Entry Action: reset PIN input buffer; start PIN entry timer)")
    step += 1

    # State: WAITING FOR PIN -> WAITING FOR PIN (Failure 1)
    print_step(step,
               "WAITING FOR PIN",
               "Enter PIN [PIN is incorrect AND attempts < 3]",
               "/ increment attempt counter; prompt for PIN again (Attempt 1 of 3)",
               "WAITING FOR PIN (Self-Transition)")
    step += 1

    # State: WAITING FOR PIN -> WAITING FOR PIN (Failure 2)
    print_step(step,
               "WAITING FOR PIN",
               "Enter PIN [PIN is incorrect AND attempts < 3]",
               "/ increment attempt counter; prompt for PIN again (Attempt 2 of 3)",
               "WAITING FOR PIN (Self-Transition)")
    step += 1

    # State: WAITING FOR PIN -> CARD TRAPPED (Failure 3)
    print_step(step,
               "WAITING FOR PIN",
               "Enter PIN [attempts = 3]",
               "/ trap card; display error: 'Maximum Attempts Reached'",
               "CARD TRAPPED (Entry Action: disable card reader; record session failure)")
    step += 1

    # State: CARD TRAPPED -> FINAL NODE
    print_step(step,
               "CARD TRAPPED",
               "OK (User presses button/Timeout)",
               "/ log closure notification",
               "FINAL NODE")


if __name__ == "__main__":
    successful_withdrawal_sequence()
    successful_balance_check_sequence()
    failed_authentication_sequence()
