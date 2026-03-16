# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 19:51:56 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 19:59:19 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	day = int(input("Days until harvest: "))
	for num in range(day):
		print("Day", (num + 1))
	print("Harvest time!")
if __name__ == "__main__":
	ft_count_harvest_iterative()