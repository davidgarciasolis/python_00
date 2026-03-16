# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 19:51:42 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 20:21:24 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_recursive(day):
	if (day != 1):
		ft_recursive(day - 1)
	print("Day", day)
def	ft_count_harvest_recursive():
	day = int(input("Days until harvest: "))
	ft_recursive(day)
	print("Harvest time!")
if __name__ == "__main__":
	ft_count_harvest_recursive()
	