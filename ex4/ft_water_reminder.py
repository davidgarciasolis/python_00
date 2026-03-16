# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 19:46:54 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 19:50:21 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	day = int(input("Days since last watering: "))
	if (day > 2):
		print("Water the plants!")
	else:
		print("Plants are fine")
if __name__ == "__main__":
	ft_water_reminder()