# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 19:38:15 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 19:44:50 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if (age > 60):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
if __name__ == "__main__":
	ft_plant_age()