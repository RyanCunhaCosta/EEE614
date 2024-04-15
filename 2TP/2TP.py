import matplotlib.pyplot as plt

# Initial values for the previous errors and outputs
prev_input_1 = 0
prev_input_2 = 0
prev_output_1 = 0
prev_output_2 = 0


def discrete_transfer_function(input_value, b0, b1, b2, a1, a2):
    global prev_input_1, prev_input_2, prev_output_1, prev_output_2

    # Calculate the current output using the given coefficients and previous values
    current_output = (
        b0 * input_value
        + b1 * prev_input_1
        + b2 * prev_input_2
        - a1 * prev_output_1
        - a2 * prev_output_2
    )

    # Update previous values for next iteration
    prev_input_2 = prev_input_1
    prev_input_1 = input_value
    prev_output_2 = prev_output_1
    prev_output_1 = current_output

    return current_output


# Input value for the filter
input_value = 1
# Filter coefficients
b0 = 0.009009
b1 = 0.01802
b2 = 0.009009
a1 = -1.784
a2 = 0.8189

output = []
for _ in range(100):
    output.append(discrete_transfer_function(input_value, b0, b1, b2, a1, a2))

# Plotting the results
plt.plot(output)
plt.title("Output")
plt.savefig("2TP/output.png")
