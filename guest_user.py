import random

# ask the user for the maximum number
max_num = int(input("Masukkan angka maksimal yang dapat diinginkan: "))

# randomly choose a number to be guessed
number = random.randint(1, max_num)

# set the initial number of guesses to zero
num_guesses = 0

# prompt the user to start guessing
print("Komputer sedang berpikir tentang sebuah angka antara 1 dan", max_num)

# keep looping until the user guesses the correct number
while True:
  # get the user's guess
  guess = int(input("Masukkan tebakanmu: "))

  # increment the number of guesses
  num_guesses += 1

  # check if the guess is correct
  if guess == number:
    print("Tebakanmu benar! Angka yang komputer pikirkan adalah", number)
    print("Kamu menebaknya dalam", num_guesses, "tebakan.")
    break

  # give the user a hint if their guess was too low or too high
  elif guess < number:
    print("Tebakanmu terlalu rendah. Coba lagi.")
  elif guess > number:
    print("Tebakanmu terlalu tinggi. Coba lagi.")
