def main(logfile_name):
    # A dictionary to hold status codes and their counts
    status_counts = {}

    with open(logfile_name, 'r') as logfile:
        for line in logfile:
            tokens = line.split()
            for index, token in enumerate(tokens):
                if token.startswith("HTTP/1."):  # Check if the token is HTTP version
                    # The next token should be the status code
                    status_code = int(tokens[index + 1])
                    # Update the status code count
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1

    # Convert dictionary to list of tuples and sort by count
    sorted_status = sorted(status_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_status

# Test
print(main("example.log"))
