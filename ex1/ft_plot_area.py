# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 19:05:42 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 19:31:04 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input(("Enter width: ")))
	print("Plot area:", length * width)

if __name__ == "__main__":
    ft_plot_area()