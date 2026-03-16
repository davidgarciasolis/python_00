# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: davgarc4 <davgarc4@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/16 20:31:15 by davgarc4          #+#    #+#              #
#    Updated: 2026/03/16 20:38:39 by davgarc4         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if (unit == "packets"):
		print(seed_type.capitalize(), "seeds:", quantity, unit, "packets")
if __name__ == "__main__":
	ft_seed_inventory()