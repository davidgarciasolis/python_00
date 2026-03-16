# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 19:32:05 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 19:37:42 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	day1 = int(input("Day 1 harvest: "))
	day2 = int(input("Day 2 harvest: "))
	day3 = int(input("Day 3 harvest: "))
	print("Total harvest:", (day1 + day2 + day3))

if __name__ == "__main__":
	ft_harvest_total()