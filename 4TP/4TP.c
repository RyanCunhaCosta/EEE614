#include <xc.h>

// PIC clock configurations
#pragma config FOSC = HS   // External oscillator
#pragma config WDTE = OFF  // Watchdog Timer disabled
#pragma config PWRTE = OFF // Power-up Timer disabled
#pragma config BOREN = OFF // Brown-out Reset disabled
#pragma config LVP = OFF   // Low Voltage Programming disabled

// Definitions of pins for UART
#define TX_PIN TRISC6
#define RX_PIN TRISC7

// Oscillator frequency definition in Hz
#define _XTAL_FREQ 4000000 // Example: 4 MHz

// Baud rate definition
#define BAUD_RATE 9600

// Function to initialize UART
void UART_Init()
{
    TX_PIN = 1; // Set TX pin as output
    RX_PIN = 1; // Set RX pin as input

    // Configure SPBRG register for the desired baud rate
    SPBRG = (_XTAL_FREQ / (16 * BAUD_RATE)) - 1;

    // Enable UART, configure for asynchronous communication,
    // 8 data bits, no parity, and 1 stop bit
    TXSTAbits.SYNC = 0; // Asynchronous mode
    TXSTAbits.TXEN = 1; // Enable transmission
    RCSTAbits.SPEN = 1; // Enable UART
    RCSTAbits.CREN = 1; // Enable continuous reception
}

// Function to send a character via UART
void UART_Write(char data)
{
    while (!TXSTAbits.TRMT)
        ;         // Wait until the transmission buffer is empty
    TXREG = data; // Send the character
}

// Function to receive a character via UART
char UART_Read()
{
    while (!PIR1bits.RCIF)
        ;         // Wait until a character is received
    return RCREG; // Return the received character
}

// Main function
void main()
{
    char input;

    UART_Init(); // Initialize UART

    while (1)
    {
        input = UART_Read(); // Read the received character

        // Check if the received character is a lowercase letter
        if (input >= 'a' && input <= 'z')
        {
            // Convert to uppercase and send back via UART
            UART_Write(input - 'a' + 'A');
        }
        else
        {
            // If it's not a lowercase letter, just send the character back
            UART_Write(input);
        }
    }
}
