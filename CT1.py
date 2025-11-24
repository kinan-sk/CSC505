#fantasy football watchlist
def watchlist_manager():

    player_watchlist = []
    
    print("Fantasy Fottball Watchlist")
    
    while True:
        print("\n--- Watchlist Menu ---")
        print("1: Add a player to the watchlist")
        print("2: View current watchlist")
        print("3: Remove a player from the watchlist")
        print("4: Quit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ").strip()
        
        if choice == '1':
            new_player = input("Enter the player's name to add: ").strip()
            if new_player: 
                new_player_formatted = new_player.title()
                player_watchlist.append(new_player_formatted)
                print(f"'{new_player_formatted}' has been added to the watchlist.")
            else:
                print("Player name cannot be empty.")
                
        elif choice == '2':
            if player_watchlist:
                print("\n--- Current Watchlist ---")
                player_watchlist.sort()
                for index, player in enumerate(player_watchlist, start=1):
                    print(f"{index}. {player}")
                print("-------------------------")
            else:
                print("Your watchlist is currently empty.")

        elif choice == '3':
            if not player_watchlist:
                print("The watchlist is empty. Nothing to remove.")
                continue # main menu return fxn

            # display fxn
            print("\n--- Current Watchlist for Removal ---")
            player_watchlist.sort() # sort fxn
            for index, player in enumerate(player_watchlist, start=1):
                print(f"{index}. {player}")
            print("-----------------------------------")
            
            player_to_remove = input("Enter the full name of the player to remove: ").strip().title()
            
            if player_to_remove in player_watchlist:
                player_watchlist.remove(player_to_remove)
                print(f"'{player_to_remove}' has been successfully removed from the watchlist.")
            else:
                print(f"Error: '{player_to_remove}' was not found on the watchlist.")
                
        elif choice == '4':
            # Quit fxn
            print("Watchlist Management Complete")
            break 
            
        else:
            # For invalid inputs
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    watchlist_manager()