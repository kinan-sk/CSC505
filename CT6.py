import math
import sys
from typing import List, Optional

# ==============================================================================
# I. THE STEPWISE REFINEMENT ALGORITHM (Design Outline)
# 
# This section outlines the Check Writer algorithm using the three levels of 
# procedural abstraction, representing the design phase of the Stepwise 
# Refinement Approach before the detailed implementation.
# ==============================================================================

# ------------------------------------------------------------------------------
# A. LEVEL 1 ABSTRACTION: System Interface (The Goal)
# Procedure: write_amount_in_words(amount)
# Orchestrates the overall conversion from number to formatted check string.
# ------------------------------------------------------------------------------
# 1. PARSE the input 'amount' into its integer dollar and integer cent components. [Calls L2: _parse_amount]
# 2. CONVERT the integer dollar component into words, handling magnitude groups. [Calls L2: _convert_dollars]
# 3. CONVERT the integer cent component into a fractional string (XX/100). [Calls L2: _convert_cents]
# 4. ASSEMBLE the final string: Concatenate dollar words, " and ", cent fraction, and " DOLLARS".
# 5. RETURN the formatted string.

# ------------------------------------------------------------------------------
# B. LEVEL 2 ABSTRACTION: Major Component Delegation (Structure & Magnitude)
# These procedures manage the structural flow and delegation of complex tasks.
# ------------------------------------------------------------------------------

# Procedure: _parse_amount(amount)
# 1. Separate the float 'amount' into an integer dollar component and an integer cent component (0-99).
# 2. Return (dollars, cents).

# Procedure: _convert_dollars(dollars)
# 1. Loop through the integer 'dollars' in 3-digit groups (e.g., hundreds, thousands, millions).
# 2. For each 3-digit group, CONVERT the block to words. [Calls L3: _convert_three_digits]
# 3. APPEND the appropriate magnitude name (e.g., "Thousand", "Million") to the words.
# 4. Assemble and return the words in the correct magnitude order.

# Procedure: _convert_cents(cents)
# 1. Format the integer 'cents' (0-99) as a two-digit zero-filled string.
# 2. Return the string in the required fraction format (XX/100).

# ------------------------------------------------------------------------------
# C. LEVEL 3 ABSTRACTION: Core Primitives (Reusable Refinement Logic)
# These procedures provide the fundamental, highly reusable number-to-word logic.
# ------------------------------------------------------------------------------

# Procedure: _convert_three_digits(n)
# 1. If 'n' is >= 100, convert the hundreds digit and append "Hundred".
# 2. Convert the remainder (0-99) into words. [Calls L3: _convert_two_digits]
# 3. Return the combined words.

# Procedure: _convert_two_digits(n)
# 1. Handle single digits (0-9) via lookup.
# 2. Handle teens (10-19) via lookup.
# 3. Handle numbers 20-99 by separating tens and ones digits and joining the words via lookups.
# 4. Return the words.


# ==============================================================================
# II. CONSTANTS / LOOKUP TABLES (Used by Level 3 Primitives)
# ==============================================================================

ONES_WORDS = {
    0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}

TEENS_WORDS = {
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}

TENS_WORDS = {
    2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 
    6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
}

# The names for the magnitude blocks
MAGNITUDES = ["", "Thousand", "Million", "Billion", "Trillion"] 

# ==============================================================================
# III. LEVEL 3 ABSTRACTION: CORE PRIMITIVES (0 - 999 Conversion)
# Most refined, reusable logic blocks.
# ==============================================================================

def _convert_two_digits(n: int) -> str:
    """
    [L3] Converts a number from 0 to 99 into words. (Core Primitive)
    """
    if n == 0:
        return ""
    if 0 < n < 10:
        return ONES_WORDS[n]
    if 10 <= n < 20:
        return TEENS_WORDS[n]
    
    # Numbers >= 20
    tens_digit = n // 10
    ones_digit = n % 10
    
    tens_part = TENS_WORDS.get(tens_digit, "")
    ones_part = ONES_WORDS.get(ones_digit, "")

    # Handles hyphenation if needed, simple space is common for checks
    result = (tens_part + " " + ones_part).strip()
    return result

def _convert_three_digits(n: int) -> str:
    """
    [L3] Converts a number from 0 to 999 into words. 
    (Refinement: It calls the L3 primitive _convert_two_digits.)
    """
    if n == 0:
        return ""

    hundreds_digit = n // 100
    remainder = n % 100
    
    parts: List[str] = []

    if hundreds_digit > 0:
        parts.append(f"{ONES_WORDS[hundreds_digit]} Hundred")

    if remainder > 0:
        # Calls the lower-level L3 primitive: _convert_two_digits
        parts.append(_convert_two_digits(remainder))

    return " ".join(parts).strip()


# ==============================================================================
# IV. LEVEL 2 ABSTRACTION: MAJOR COMPONENT DELEGATION
# Breaks down the total amount into its constituent parts.
# ==============================================================================

def _convert_dollars(dollars: int) -> str:
    """
    [L2] Converts a large integer (the dollar amount) into words 
    by breaking it into 3-digit groups (blocks) and appending magnitude names.
    (Delegation: This function calls the L3 primitive: _convert_three_digits.)
    """
    if dollars == 0:
        return "Zero"

    words: List[str] = []
    i = 0  # Magnitude index 
    temp_dollars = dollars
    
    while temp_dollars > 0 and i < len(MAGNITUDES):
        three_digit_block = temp_dollars % 1000 
        
        if three_digit_block > 0:
            # Calls the L3 primitive to convert the block to words
            block_words = _convert_three_digits(three_digit_block)
            magnitude_name = MAGNITUDES[i]
            
            # Add magnitude only if it's not the ones block (i > 0)
            if i > 0:
                words.append(f"{block_words} {magnitude_name}")
            else:
                words.append(block_words)

        temp_dollars //= 1000
        i += 1
    
    # Reverse to get correct order
    return " ".join(reversed(words)).strip()


def _convert_cents(cents: int) -> str:
    """
    [L2] Converts the 2-digit cent amount into the required fraction format.
    """
    cents_str = str(cents).zfill(2) 
    return f"{cents_str}/100"


def _parse_amount(amount: float) -> tuple[int, int]:
    """
    [L2] Separates a float amount into its dollar and cent components.
    """
    dollars = int(amount)
    # Use careful rounding to avoid floating-point errors
    cents = int(round((amount - dollars) * 100))
    
    return dollars, cents


# ==============================================================================
# V. LEVEL 1 ABSTRACTION: MAIN SYSTEM INTERFACE (The Final Goal)
# Orchestrates the Level 2 components to deliver the final result.
# ==============================================================================

def write_amount_in_words(amount: float) -> str:
    """
    [L1] The highest level of abstraction. Given a numeric amount, it returns 
    the full, formatted check amount in words.
    
    (Orchestration: Calls the L2 primitives: _parse_amount, _convert_dollars, _convert_cents.)

    Args:
        amount: The total numeric dollar amount (e.g., 1234.56).

    Returns:
        The final formatted string for the check (e.g., "One Thousand Two Hundred Thirty Four and 56/100").
    """
    if amount < 0:
        return "ERROR: Negative amounts are not supported for check writing."
    
    # 1. Calls L2 to break the amount down
    dollars, cents = _parse_amount(amount) 
    
    # 2. Calls L2 to convert the dollar part
    dollar_words = _convert_dollars(dollars)
    
    # 3. Calls L2 to convert the cent part
    cent_fraction = _convert_cents(cents)
    
    # 4. Assembles the final, formatted output
    return f"{dollar_words} and {cent_fraction}"


# ==============================================================================
# VI. EXECUTION BLOCK
# Handles user interaction to demonstrate the final algorithm.
# ==============================================================================

if __name__ == "__main__":
    print("--- Check Writer Program (Stepwise Refinement Demo) ---")
    
    # Example test cases
    test_cases = [
        371.18,         # Covers Hundreds, Tens, and Teens (71, 18)
        42598.05,       # Covers Thousands and a small cent value
        8000.00,        # Exact thousands boundary
        19.99,          # Teens and high cents
        0.47,           # Zero dollars
        7654321.10      # Millions, demonstrating magnitude logic
    ]
    
    for test_amount in test_cases:
        try:
            result = write_amount_in_words(test_amount)
            # Formatting to match the Execution PDF output for clarity
            print(f"\nNumeric Amount: $ {test_amount:,.2f}") 
            print(f"Written Amount: {result} DOLLARS")
        except Exception as e:
            # Simple error handling
            print(f"Error processing {test_amount}: {e}", file=sys.stderr)
            
    print("\n----------------------------------------------------")
    print("Execution complete.")