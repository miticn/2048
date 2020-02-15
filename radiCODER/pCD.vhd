library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity pCD is
	port
	(
		-- Input ports
		I3	: in std_logic;
		I2	: in std_logic;
		I1	: in std_logic;
		I0	: in std_logic;
		E: in std_logic;

		-- Output ports
		Z0	: out std_logic;
		Z1	: out std_logic;
		W	: out std_logic
	);
end;

architecture rtl of pCD is
begin
    
	process (I3, I2, I1, I0) is
	begin
		if(E = '1') then
		if (I3 = '1') then 
			Z0 <= '1';
			Z1 <= '1';
			W <= '1';
		else
			if(I2 = '1')then 
				Z0 <= '0';
				Z1 <= '1';
				W <= '1';
			elsif(I1 = '1')then 
				Z0 <= '1';
				Z1 <= '0';
				W <= '1';
			elsif(I0 = '1')then 
				Z0 <= '0';
				Z1 <= '0';
				W <= '1';
			else
				Z0 <= '0';
				Z1 <= '0';
				W <= '0';
			end if;
		end if;
		else 
			Z0 <= '0';
			Z1 <= '0';
			W <= '0';
		end if;
	end process;

end;

