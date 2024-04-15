#include <xc.h>
#include <stdint.h>

// Define global variables for previous inputs and outputs
float prev_input_1 = 0;
float prev_input_2 = 0;
float prev_output_1 = 0;
float prev_output_2 = 0;

// Function to calculate the discrete transfer function
float discrete_transfer_function(float input_value, float b0, float b1, float b2, float a1, float a2)
{
    // Calculate the current output using the given coefficients and previous values
    float current_output =
        (b0 * input_value) +
        (b1 * prev_input_1) +
        (b2 * prev_input_2) -
        (a1 * prev_output_1) -
        (a2 * prev_output_2);

    // Update previous values for next iteration
    prev_input_2 = prev_input_1;
    prev_input_1 = input_value;
    prev_output_2 = prev_output_1;
    prev_output_1 = current_output;

    return current_output;
}

void main()
{
    // Input value for the filter
    float input_value = 1;
    // Filter coefficients
    float b0 = 0.009009;
    float b1 = 0.01802;
    float b2 = 0.009009;
    float a1 = -1.784;
    float a2 = 0.8189;

    // Output array
    float output[100];
    int i;

    // Calculate output for 100 iterations
    for (i = 0; i < 100; i++)
    {
        output[i] = discrete_transfer_function(input_value, b0, b1, b2, a1, a2);
    }
}
