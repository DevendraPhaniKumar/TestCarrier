from Lib_space import Local_UI as A
class UI():

    def ethernet(self):
        A.init_ssh()
        A.cmd_ssh("login root")  # login as root
        A.cmd_ssh("X*rD8u!6nk")  # root Password
        A.dismiss_modal_window()  #
        # Ethernet 0 Configuration Change *************************************************
        A.click(37, 37)                             # Click Operation on home Button
        A.click(640,24)                             # Click on lock
        A.click(182,310)                            # Click on Factory Login
        A.click(604,366)                            # Click on Login
        A.Write_Field("113")                        # Entering Password
        A.click(37, 37)                             # Click Operation on home Button
        A.click(156,33)                             # Click Operation on Main Menu
        A.click(776,455)                            # Click Operation on Down Navigation Arrow
        A.click(137,112)                            # Click Operation on Configuration Menu
        A.click(144,100)                            # Click Operation on HMI Configuration
        A.click(136,108)                            # Click Operation on Ethernet-0 icon
        A.click(510,90)                             # Click interface eth0
        A.click(426,232)                            # For Static Selection
        A.click(419,456)                            # Click Operation on Configure button
        A.click(527,78)                             # Click Operation on IP Address Block
        A.Field_Clear(16)                           # Clear previous IP Address
        A.Write_Field("169.254.1.1")                # Enter IP Address
        #A.click(583,350)                           # Click Done in keypad
        A.click(527,113)                            # Click on Subnet Mask
        A.Field_Clear(16)                           # Clear previous IP Address
        A.Write_Field("255.255.255.0")              # Enter Subnet Mask Address
        #A.click(583,350)                           # Click Done in keypad
        A.click(695,210)                            # Click on Save Button
        A.click(610,265)                            # Click on Gateway block
        A.Field_Clear(16)                           # Clear Previous Data
        A.Write_Field("0.0.0.0")                    # Enter Gate Way Address
        A.click(610,311)                            # Click on GW1 Dest/Mask block
        A.Field_Clear(16)                           # Clear Previous Data
        A.Write_Field("0.0.0.0/0")                    # Enter GW1 Dest/Mask Way Address
        A.click(418,358)                            # Click on Not Apply Button
        A.click(428,243)                            # Click on  Apply Option
        A.click(778,460)                            # Click on Down Navigation Arrow
        A.click(409,221)                            # Click on DNS IP Config Button
        A.click(595,123)                            # Click in DSN 1 Server Block
        A.Field_Clear(16)                           # Clear previous DSN 1 Address
        A.Write_Field("192.168.100.1")              # Enter DSN 1 Server Address
        A.click(609,164)                            # Click in DSN 2 Server Block
        A.Field_Clear(16)                           # Clear previous DSN 2 Address
        A.Write_Field("192.168.100.1")              # Enter DSN 2 Server Address
        A.click(646,216)                            # Click on Save Button
        # Ethernet 1 Configuration Change *************************************************
        A.click(99,26)                              # Click on Back Button
        A.click(99,26)                              # Click on Back Button
        A.click(99,26)                              # Click on Back Button
        A.click(99,26)                              # Click on Back Button
        A.click(396,122)                            # Click Operation on Ethernet-1 icon
        A.click(510,90)                             # Click interface eth1
        A.click(426,232)                            # For Static Selection
        A.click(419,456)                            # Click Operation on Configure button
        A.click(527,78)                             # Click Operation on IP Address Block
        A.Field_Clear(16)                           # Clear previous IP Address
        A.Write_Field("192.168.100.10")                # Enter IP Address
        #A.click(583,350)                           # Click Done in keypad
        A.click(527,113)                            # Click on Subnet Mask
        A.Field_Clear(16)                           # Clear previous IP Address
        A.Write_Field("255.255.255.0")              # Enter Subnet Mask Address
        #A.click(583,350)                           # Click Done in keypad
        A.click(695,210)                            # Click on Save Button
        A.click(599,282)                            # Click on Gateway block
        A.Field_Clear(16)                           # Clear Previous Data
        A.Write_Field("192.168.100.1")              # Enter Gate Way Address
        A.click(610,311)                            # Click on GW1 Dest/Mask block
        A.Field_Clear(16)                           # Clear Previous Data
        A.Write_Field("0.0.0.0/0")                    # Enter GW1 Dest/Mask Way Address
        A.click(418,358)                            # Click on Not Apply Button
        A.click(428,243)                            # Click on  Apply Option
        A.click(778,460)                            # Click on Down Navigation Arrow
        A.click(409,221)                            # Click on DNS IP Config Button
        A.click(595,123)                            # Click in DSN 1 Server Block
        A.Field_Clear(16)                           # Clear previous DSN 1 Address
        A.Write_Field("192.168.100.1")              # Enter DSN 1 Server Address
        A.click(609,164)                            # Click in DSN 2 Server Block
        A.Field_Clear(16)                           # Clear previous DSN 2 Address
        A.Write_Field("192.168.100.1")              # Enter DSN 2 Server Address
        A.click(656,228)                            # Click on Save Button
        # Network Diagnostics
        A.click(99,26)                              # Click on Back Button
        A.click(99,26)                              # Click on Back Button
        A.click(99,26)                              # Click on Back Button
        A.click(99,26)                              # Click on Back Button
        A.click(776,461)                            # Click on Down Arrow
        A.click(136,255)                            # Click on Network Diagnostics icon
        A.click(560,243)                            # Click on Server Address block
        A.Field_Clear(16)                           # Clear previous Server Address
        A.Write_Field("google.com")                 # Enter Server Address
        A.click(480,272)                            # Click on Interface block
        A.click(417,247)                            # Click on Eth-0
        A.click(410,448)                            # Click on Run Cloud Test
        A.click(411,319)                            # Click on Run Ping Test
        A.click(37, 37)                             # Click Operation on home Button


        A.close_ssh()
