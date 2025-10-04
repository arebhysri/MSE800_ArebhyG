"""Analyze user input (string or list of strings) for length and uppercase character count."""
class AnalyzeCode:
    """Analyzes input data for total length and number of uppercase characters."""
    def __init__(self, data):
        """Initialize with a string or list of strings."""
        self.data = data

    def count_total_length(self):
        """Return the total length of the input data."""
        return len(self.data)

    def count_uppercase_characters(self):
        """Count uppercase characters in a string or list of strings."""
        if isinstance(self.data, str):
            return sum(1 for char in self.data if char.isupper())
        elif isinstance(self.data, list):
            return sum(
                1 for item in self.data if isinstance(item, str)
                for char in item if char.isupper()
            )
        raise ValueError("Input should be a string or list of strings")
        
def main():
    """Read the input from user"""
    input_data = input("Enter a string or comma-separated list of strings: ")
    if ',' in input_data:
        data = [item.strip() for item in input_data.split(',')]
    else:
        data = input_data.strip()
    analyzer = AnalyzeCode(data)
    total_length = analyzer.count_total_length()
    upper_count = analyzer.count_uppercase_characters()
    
    print(f"Total Length: {total_length}")
    print(f"Number of Uppercase Characters: {upper_count}")

if __name__ == "__main__":
    main()
    