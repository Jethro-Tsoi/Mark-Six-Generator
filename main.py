from itertools import combinations
import random
from typing import List, Set, Dict, Tuple
from enum import Enum, auto
from dataclasses import dataclass

from CombinationType import CombinationType

class Language(Enum):
    EN = auto()
    ZH = auto()

class Translations:
    STRINGS = {
        'title': {
            Language.EN: "Mark Six Smart Combinations Generator",
            Language.ZH: "六合彩聰明組合生成器"
        },
        'available_combinations': {
            Language.EN: "Available combinations:",
            Language.ZH: "可用的組合:"
        },
        'select_combination': {
            Language.EN: "Select combination type (1-40): ",
            Language.ZH: "選擇組合類型 (1-40): "
        },
        'select_mode': {
            Language.EN: "Select mode (1: Random, 2: Custom): ",
            Language.ZH: "選擇模式 (1: 隨機, 2: 自定義): "
        },
        'enter_numbers': {
            Language.EN: "Enter {} numbers (1-49): ",
            Language.ZH: "請輸入{}個號碼 (1-49): "
        },
        'selected_numbers': {
            Language.EN: "Selected numbers",
            Language.ZH: "已選擇的號碼"
        },
        'generated_combinations': {
            Language.EN: "Generated combinations:",
            Language.ZH: "產生的組合:"
        },
        'error': {
            Language.EN: "Error",
            Language.ZH: "錯誤"
        },
        'invalid_combination': {
            Language.EN: "Invalid combination type",
            Language.ZH: "無效的組合類型"
        }
    }

    @staticmethod
    def get(key: str, lang: Language, *args) -> str:
        text = Translations.STRINGS[key][lang]
        if args:
            return text.format(*args)
        return text

class SmartCombination:
    def __init__(self, language: Language = Language.EN):
        self.all_numbers = set(range(1, 50))  # Hong Kong Mark Six uses numbers 1-49
        self.language = language

    def validate_numbers(self, selected_numbers: List[int], combo_type: CombinationType) -> bool:
        """Validate the input numbers"""
        numbers_set = set(selected_numbers)
        required_count = combo_type.input_count
        
        if len(numbers_set) != required_count:
            return False
        if not numbers_set.issubset(self.all_numbers):
            return False
        return True

    def generate_combinations(self, selected_numbers: List[int], combo_type: CombinationType) -> List[List[int]]:
        """Generate combinations based on the specified type"""
        if not self.validate_numbers(selected_numbers, combo_type):
            raise ValueError(f"Please select exactly {combo_type.input_count} different numbers between 1 and 49")

        selected_numbers = sorted(selected_numbers)
        return [[selected_numbers[i] for i in pattern] for pattern in combo_type.patterns]

    def get_combination_info(self, combo_type: CombinationType) -> str:
        """Get formatted information about a combination type"""
        return (f"Smart Combination {combo_type.name.split('_')[1]} "
                f"({combo_type.input_count:02d}-{combo_type.output_count:02d}, "
                f"{combo_type.match_guarantee[0]}/{combo_type.match_guarantee[1]})")

def format_combination(combo: List[int]) -> str:
    """Format a combination for display"""
    return " ".join(f"{num:02d}" for num in combo)

def main():
    language = Language.ZH  # This could be configurable
    smart_combo = SmartCombination(language)
    
    print(Translations.get('title', language))
    print("\n" + Translations.get('available_combinations', language))
    
    for combo_type in CombinationType:
        print(f"{combo_type.name.split('_')[1]}. {smart_combo.get_combination_info(combo_type)}")
    
    try:
        combo_input = input(Translations.get('select_combination', language))
        combo_type = next(ct for ct in CombinationType 
                         if ct.name == f"SMART_{int(combo_input):02d}")
        
        mode = input(Translations.get('select_mode', language))
        
        if mode == "1":
            input_numbers = random.sample(range(1, 50), combo_type.input_count)
        else:
            prompt = Translations.get('enter_numbers', language, combo_type.input_count)
            input_numbers = [int(num) for num in input(prompt).split()]
            
        print(f"\n{Translations.get('selected_numbers', language)}: {format_combination(input_numbers)}")
        
        combinations = smart_combo.generate_combinations(input_numbers, combo_type)
        
        print("\n" + Translations.get('generated_combinations', language))
        for i, combo in enumerate(combinations, 1):
            print(f"[{i:02d}] {format_combination(combo)}")
            
    except ValueError as e:
        print(f"{Translations.get('error', language)}: {e}")
    except StopIteration:
        print(Translations.get('invalid_combination', language))

if __name__ == "__main__":
    main()
