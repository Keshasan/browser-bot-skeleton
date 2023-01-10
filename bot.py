from cls.BrowsserBot import Bot


def main():
    bot = Bot()
    bot.google_test()
    bot.save_cookies()


if __name__ == "__main__":
    main()
