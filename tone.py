from machine import PWM, Pin
import time

# Define the pin number for the buzzer
buzzer_pin = Pin(12)

# Define the PWM object with the buzzer pin
buzzer_pwm = PWM(buzzer_pin)

# Dictionary mapping note names to their corresponding frequencies
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523,
}

# Function to play a note
def play_note(note, duration):
    frequency = notes.get(note)
    if frequency:
        buzzer_pwm.freq(frequency)  # Set the frequency of the PWM
        buzzer_pwm.duty(512)  # Set the duty cycle to 50% (midpoint)
        time.sleep(duration)  # Play the note for the specified duration
        buzzer_pwm.duty(0)  # Turn off the buzzer

# Example usage
play_note('C4', 0.5)  # Play C4 for 0.5 seconds
play_note('E4', 1)  # Play E4 for 1 second
play_note('G4', 2)  # Play G4 for 2 seconds
