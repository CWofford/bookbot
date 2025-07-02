def split_words(text):
    return len(text.split()) 
def times_char_appears(text):
    lower = text.lower()
    return {char: lower.count(char) 
    for char in set(lower) if char.isalpha()}
def sort_report(report):
    sorted_report = sorted(report.items(), key=lambda item: item[1], reverse=True)
    report_str = "\n".join(f"{char}: {count}" for char, count in sorted_report)
    return report_str 