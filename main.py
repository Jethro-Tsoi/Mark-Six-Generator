from itertools import combinations
import random
from typing import List, Set

class SmartCombination:
    def __init__(self):
        self.all_numbers = set(range(1, 50))  # Hong Kong Mark Six uses numbers 1-49
        
    def validate_numbers(self, selected_numbers: List[int]) -> bool:
        """Validate the input numbers"""
        numbers_set = set(selected_numbers)
        if len(numbers_set) != 10:
            return False
        if not numbers_set.issubset(self.all_numbers):
            return False
        return True

    def generate_combinations_9(self, selected_numbers: List[int]) -> List[List[int]]:
        """
        Generate Smart Combination 9 (10-16, 5/6)
        Input: 10 numbers
        Output: 16 combinations of 6 numbers each
        """
        if not self.validate_numbers(selected_numbers):
            raise ValueError("Please select exactly 10 different numbers between 1 and 49")

        # Sort input numbers for consistent output
        selected_numbers = sorted(selected_numbers)
        
        # The specific combination pattern for Smart Combination 9
        combinations_9 = [
            [0, 1, 2, 3, 4, 5],    # 01 02 03 04 05 06
            [1, 2, 3, 6, 7, 9],    # 02 03 04 07 08 10
            [0, 2, 3, 6, 8, 9],    # 01 03 04 07 09 10
            [0, 1, 3, 5, 7, 8],    # 01 02 04 06 08 09
            [1, 2, 4, 6, 7, 8],    # 02 03 05 07 08 09
            [0, 1, 4, 5, 6, 9],    # 01 02 05 06 07 10
            [0, 2, 4, 5, 7, 9],    # 01 03 05 06 08 10
            [0, 1, 3, 4, 8, 9],    # 01 02 04 05 09 10
            [0, 2, 5, 6, 7, 8],    # 01 03 06 07 08 09
            [1, 2, 5, 7, 8, 9],    # 02 03 06 08 09 10
            [0, 3, 4, 5, 6, 7],    # 01 04 05 06 07 08
            [0, 4, 6, 7, 8, 9],    # 01 05 07 08 09 10
            [2, 3, 4, 5, 7, 8],    # 03 04 05 06 08 09
            [1, 3, 5, 6, 8, 9],    # 02 04 06 07 09 10
            [1, 3, 4, 5, 7, 9],    # 02 04 05 06 08 10
            [2, 4, 5, 6, 8, 9]     # 03 05 06 07 09 10
        ]
        
        # Convert index-based combinations to actual numbers
        result = []
        for combo in combinations_9:
            actual_numbers = [selected_numbers[i] for i in combo]
            result.append(actual_numbers)
            
        return result

def format_combination(combo: List[int]) -> str:
    """Format a combination for display"""
    return " ".join(f"{num:02d}" for num in combo)

def main():
    smart_combo = SmartCombination()
    
    print("香港六合彩聰明組合 9 (10-16, 5/6)")
    
    try:
        mode = input("請選擇模式 (1: 隨機, 2: 自定義): ")
        if mode == "1":
            input_numbers = random.sample(range(1, 50), 10)
        else:
            input_numbers = input("請輸入10個號碼 (1-49): ")
            input_numbers = [int(num) for num in input_numbers.split()]
        print(f"\n已選擇的號碼: {format_combination(input_numbers)}")
        
        combinations = smart_combo.generate_combinations_9(input_numbers)
        
        print("\n產生的組合:")
        for i, combo in enumerate(combinations, 1):
            print(f"[{i:02d}] {format_combination(combo)}")
            
    except ValueError as e:
        print(f"錯誤: {e}")

if __name__ == "__main__":
    main()
