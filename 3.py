
seconds = int(input("Введіть кількість секунд: "))


if seconds < 0 or seconds >= 8640000:
    print("Число повинно бути більше або дорівнювати 0 і менше ніж 8640000.")
else:

    days, seconds = divmod(seconds, 86400)


    hours, seconds = divmod(seconds, 3600)


    minutes, seconds = divmod(seconds, 60)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    print(f"{days} {'день' if days == 1 else 'днів'}, {hours}:{minutes}:{seconds}")
