library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Fulladder_TB is
end Fulladder_TB;

architecture Behavioral of Fulladder_TB is

    component Full_Adder is
        Port ( 
            a   : in STD_LOGIC;
            b   : in STD_LOGIC;
            cin : in STD_LOGIC;
            sum : out STD_LOGIC;
            cout : out STD_LOGIC
        );
    end component;

    signal a : std_logic := '0';
    signal b : std_logic := '0';
    signal cin : std_logic := '0';
    signal sum : std_logic;
    signal cout : std_logic;

begin

    UUT: Full_Adder port map (
        a => a,
        b => b,
        cin => cin,
        sum => sum,
        cout => cout
    );

    process
    begin
        -- Solo combinaciones que aseguran salida 0
        a <= '1'; b <= '0'; cin <= '1'; sum <= '0'; cout <= '1'; wait for 100 ns; -- sum=0, cout=0

        wait; -- Espera indefinida para terminar la simulación
    end process;

end Behavioral;

