# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 20:11:53 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 20:23:30 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_garden_summary():
	Garden = input("Enter garden name: ")
	Plants = input("Enter number of plants: ")
	print("Garden: ", Garden)
	print("Plants: ", Plants)
	print("Status: Growing well!")
if __name__ == "__main__":
	ft_garden_summary()