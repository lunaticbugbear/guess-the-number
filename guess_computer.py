import random

# prompt the user to enter the maximum number that can be guessed
max_num = int(input("Masukkan angka terbesar yang diinginkan: "))

# randomly choose a number to be guessed
number = random.randint(1, max_num)

# set the initial number of guesses to zero
num_guesses = 0

# set the initial range of possible numbers to be all numbers between 1 and max_num
low = 1
high = max_num

# prompt the user to start guessing
print("Sedang mengacak sebuah angka antara 1 dan", max_num)

# keep looping until the computer guesses the correct number
while True:
  # have the computer make a guess
  guess = (low + high) // 2

  # increment the number of guesses
  num_guesses += 1

  # check if the guess is correct
  if guess == number:
    print("Komputer berhasil menebaknya! Angka acak yang kamu dapatkan adalah", number)
    print("Komputer membutuhkan", num_guesses, "tebakan untuk menebak angka yang benar.")
    break

  # give the computer a hint if its guess was too low or too high
  elif guess < number:
    print("Tebakan komputer terlalu rendah. Mengubah range angka yang memungkinkan.")
    low = guess
  elif guess > number:
    print("Tebakan komputer terlalu tinggi. Mengubah range angka yang memungkinkan.")
    high = guess
