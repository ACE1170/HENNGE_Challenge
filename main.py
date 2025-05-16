def process_test_cases(test_cases, results=None):
    if not test_cases:
        return results
    if results is None:
        results = []

    x, rest = test_cases[0], test_cases[1:]

    if len(rest) == 0:
        return results + [-1]

    numbers = rest[0].split()
    if len(numbers) != int(x):
        return process_test_cases(rest[1:], results + [-1])

    def calculate_power_of_four(nums, acc=0):
        if not nums:
            return acc
        n = int(nums[0])
        return calculate_power_of_four(nums[1:], acc + (n ** 4 if n <= 0 else 0))

    result = calculate_power_of_four(numbers)
    return process_test_cases(rest[1:], results + [result])

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()

    def run(index=1, collected=[]):
        if index >= len(input_lines):
            return process_test_cases(collected)
        return run(index + 1, collected + [input_lines[index]])

    try:
        n = int(input_lines[0])
        results = run()
        for r in results:
            print(r)
    except Exception:
        pass

if __name__ == "__main__":
    main()
