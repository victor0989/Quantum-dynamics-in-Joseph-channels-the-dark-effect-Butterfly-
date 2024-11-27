library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity RCA is
    Port (
        a    : in STD_LOGIC_VECTOR (3 downto 0);
        b    : in STD_LOGIC_VECTOR (3 downto 0);
        cin  : in STD_LOGIC;
        sum  : out STD_LOGIC_VECTOR (3 downto 0);
        cout : out STD_LOGIC
    );
end RCA;

architecture Behavioral of RCA is

    component Full_Adder is
        Port (
            a    : in STD_LOGIC;
            b    : in STD_LOGIC;
            cin  : in STD_LOGIC;
            sum  : out STD_LOGIC;
            cout : out STD_LOGIC
        );
    end component;

    signal C1, C2, C3 : STD_LOGIC;

begin

    FA1: Full_Adder port map (
        a => a(0),
        b => b(0),
        cin => cin,
        sum => sum(0),
        cout => C1
    );

    FA2: Full_Adder port map (
        a => a(1),
        b => b(1),
        cin => C1,
        sum => sum(1),
        cout => C2
    );

    FA3: Full_Adder port map (
        a => a(2),
        b => b(2),
        cin => C2,
        sum => sum(2),
        cout => C3
    );

    FA4: Full_Adder port map (
        a => a(3),
        b => b(3),
        cin => C3,
        sum => sum(3),
        cout => cout
    );

end Behavioral;
