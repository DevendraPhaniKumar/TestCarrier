from selenium.webdriver.common.by import By

class LoginPageLocatars(object):
    EMAIL = (By.ID, "nameInput")
    PASSWORD = (By.ID, "pass")
    SUBMIT = (By.ID, "submit")
    Bodytext = (By.XPATH, '//*[@id="MainBarTR"]/td[5]/div/img')
    logout = (By.XPATH, '//*[@title="System Menu"]')
    LogoutLink=(By.XPATH,'//*[@id="main_logout"]')
    frameOfLoginoverlay=(By.ID,'rightMenuiframe')

class WebCTRLPageLocators(object):
    ActionButtonSpan=(By.ID, "actButtonSpan")
    ActionButtonContainer=(By.ID,"facetButtonContainer")
    DivOfActionButton = (By.TAG_NAME, "div")
    SpanOfActionButton = (By.TAG_NAME, "span")
    DropDownArrow=(By.TAG_NAME, "img")
    TableIframe=(By.ID,'actioncategories')
    PopupTable=(By.XPATH, '//*[@id="container"]')
    DivOfActionButton2 = (By.TAG_NAME, "nobr")
    GeoTreeHead=(By.ID,'geoTree_2')
    DropDownMenu=(By.CLASS_NAME,'menuSection barBg')
    IconListId=(By.CLASS_NAME, 'buttonSection barBg')
    ActionBar=(By.XPATH,'//*[@id="actionBar"]')
    ActionBarTable=(By.TAG_NAME,"td")
    ActionBarMain=(By.XPATH, '//*[@id="MainBarTR"]')
    ActionContainer=(By.XPATH, '//*[@id="ActionContentContainer"]')
    TimeLapseWindowTable=(By.ID, 'tmCalendarModal')
    NetworkTree=(By.NAME,'navTableFrame')
    ScrollBar=(By.ID,'navVbar')

class AlarmsPage(object):
    SelectedCount = (By.XPATH, '//*[@id="SelectionCount"]')
    Schedules = (By.XPATH, '//*[@id="paddedDiv"]/table/tbody/tr[1]/td[2]/span')
    Privileges = (By.XPATH, '//*[@id="paddedDiv"]/table/tbody/tr[2]/td[2]')
    GoButton = (By.XPATH, '//*[@id="AlarmHeaderRight"]/div[3]/span/span/div')
    dropDown = (By.XPATH, '//*[@id="bodyTable"]/tbody/tr[6]/td[5]/img')

class EnerytReportLoginpage(object):
    EMAIL = (By.ID, "id_username")
    PASSWORD = (By.ID, "id_password")
    SUBMIT = (By.NAME, "submit")
    Bodytext = (By.XPATH, '//*[@id="MainBarTR"]/td[5]/div/img')
    logout = (By.XPATH, '//*[@title="System Menu"]')


class BuildingsPageLocators(object):
    BuildingsLink=(By.XPATH, '//*[@id="mainNavigationBar"]/div/div[2]/nav/ul[1]/li[2]/a')
    OrganizationName=(By.XPATH,'//*[@id="container"]/div/div/div/div[1]/div/div[2]/div[1]/span/a')
    AddBuildingButton=(By.XPATH,'//*[@id="container"]/div/div/div/div[2]/div/button')
    CancelButton=(By.XPATH,'/html/body/div[1]/div/div/div[3]/button')
    ERGatewayName = (By.XPATH, '//*[@id="container"]/div/div/div/div[1]/div/div[2]/div[2]/span/b')
    Header_Navigator = (By.XPATH, '//*[@id="mainNavigationBar"]/div/div[2]')
    Header_Links=(By.TAG_NAME, 'li')


class MeterSourcesPageLocator(object):
    Actions_Button = (By.XPATH, '//*[@id="container"]/div/div/div/div[2]/div/div/div[1]/button')
    DropDownOverlay = (By.XPATH, '/html/body/ul')
    Header_Links = (By.TAG_NAME, 'li')
    Filter_DropDownButton=(By.ID, "btn-append-to-body")
    MeterProperty=(By.CLASS_NAME, "col-lg-4")
    OverlaySystemScope=(By.XPATH,"/html/body/div[2]")
    SystemScope = (By.XPATH, "/html/body/div[2]/div[2]/div/div[2]")
    ListElements=(By.TAG_NAME,'i')
    ExpansionImage = (By.CLASS_NAME, 'tree-branch-head')
    Areas = (By.TAG_NAME, 'span')
    AreaClass = (By.TAG_NAME, 'treeitem')
    AreaClass2=(By.CLASS_NAME, 'ng-scope')
    AreaUL = (By.TAG_NAME, 'ul')
    Areali = (By.TAG_NAME, 'li')

class BuildingosLocators(object):
    SideBarLinks=(By.XPATH,'/html/body/div[1]')
    Links = (By.TAG_NAME, 'a')
    BuildingsGrid=(By.XPATH,'//*[@id="content"]/div[2]/div/div[3]/div[1]')
    #BuildingsGrid = (By.CLASS_NAME, 'fluidGrid fluidGrid--borderCollapse')
    SpecificBuilding=(By.TAG_NAME,'h3')
    NavHeader=(By.XPATH,'//*[@id="content"]/div[1]/div/nav')
    DeleteButton=(By.ID,'deleteBuilding')
    DeleteDialog=(By.ID,'deleteModal')
    DeleteButtonOnDialog=(By.TAG_NAME,'button')


class EquipmentTouchPageLocators(object):
    HomeIcon=(By.XPATH,"((//*[@contentDescription='Home IP System']/*[@class='android.view.View'])[1]/*[@class='android.widget.Button'])[1]")
    IPButton=(By.XPATH,"//*[@contentDescription='IP' and @class='android.widget.Button']")
    SystemButton=(By.XPATH,"//*[@contentDescription='System' and @class='android.widget.Button']")
    AssignedIPAddress=(By.XPATH,"//*[@contentDescription='Assigned IP Address:' and @class='android.widget.EditText']")
    AssignedSubnetMask=(By.XPATH,"//*[@contentDescription='Assigned Subnet Mask:' and @class='android.widget.EditText']")
    #AssignedGatewayAddress=(By.XPATH,"//*[@contentDescription='Assigned Gateway IP Addr:' and @class='android.widget.EditText']")
    AssignedGatewayAddress=(By.XPATH,"//*[@content-desc='Assigned Gateway IP Address:']")
    IPNetworkNumber=(By.XPATH,"//*[@contentDescription='IP Network:' and @class='android.widget.EditText']")
    SaveButton=(By.XPATH,"//*[@contentDescription='Save']")
    CancelButton = (By.XPATH, "//*[@contentDescription='Cancel']")
    OKButton=(By.XPATH,"//*[@contentDescription='OK']")
    AppiumServerURL= "http://localhost:4723/wd/hub"
    ErrorMessage=(By.XPATH,"//*[@contentDescription='Enter number between 0 and 65534 for IP Network.']")
    IPPageTextverification=(By.XPATH,"//*[@contentDescription='Settings']")
    Output_override=(By.XPATH,"//*[@contentDescription='800.00']")
    Output_override2=(By.XPATH,"//*[@class='android.webkit.WebView' and ./*[@contentDescription='Home 800.00 Output Override= Output Override Lock= Number Control: 200.00 OK Cancel OK Cancel']]")
    SettingsHomeIcon=(By.XPATH,"//*[@contentDescription='I']")
    IPHOmeButton=(By.XPATH,"((//*[contains(@contentDescription,'Settings IP')]/*[@class='android.view.View'])[1]/*[@class='android.widget.Button'])[1]")
    
    
    


class AmazonAPP(object):
    BurgerIcon=(By.XPATH,"//*[@id='action_bar_burger_icon']")
    DropDownContainer=(By.ID,"gno_drawer_list")
    Container=(By.ID,"gno_menu_container")
    ShopByCategory=(By.XPATH,"//*[@text='Your Orders']")
    RegisterRadioButton=(By.XPATH,"//*[@id='register_accordion_header']")
    LoginRadioButton=(By.XPATH,"//*[@id='login_accordion_header']")
    Links = (By.TAG_NAME, 'text')
    ParentXpath=(By.XPATH,"./..")
    NameField=(By.XPATH,"//*[@id='ap_customer_name']")
    RegistrationPage=(By.XPATH,"//*[@text='Welcome']")
    CheckBox=(By.ID,"auth-register-show-password-checkbox")
    AuthCountryPicker=(By.ID, "auth-country-picker-container")


class Emulator(object):
    GotItLink=(By.ID, 'welcome_tour_got_it')
    LearnMore=(By.ID,'setup_addresses_title')
    AddAnEmail=(By.ID,'setup_addresses_add_another')

class EQT2(object):
    OccHeat=(By.XPATH,"//*[@contentDescription='Occ Heat']")
    OccCool=(By.XPATH,"//*[@contentDescription='Occ Cool']")
    UnoccHeat=(By.XPATH,"//*[@contentDescription='Unocc Heat']")
    UnoccCool=(By.XPATH,"//*[@contentDescription='Unocc Cool']")
    OccHeat_value=(By.XPATH,"//*[@index='7']")
    OccHeat_value_text=(By.XPATH,"//*[@index='3']")
    
    OccCool_value=(By.XPATH,"//*[@contentDescription='Occ Cool'and @class='android.widget.EditText']")
    OK=(By.XPATH,"//*[@contentDescription='OK' and @class='android.view.View']")
    count=(By.CLASS_NAME, "android.view.View")
    
    System=(By.XPATH,"//*[@contentDescription='System' and @class='android.view.View']")
    Password=(By.XPATH,"//*[@class='android.widget.EditText']")
    Login=(By.XPATH,"//*[@contentDescription='Log in']")
    Logout=(By.XPATH,"//*[@contentDescription='Log out']")
    Router=(By.XPATH,"//*[@contentDescription='Router' and @class='android.view.View']")
    IP=(By.XPATH,"//*[@contentDescription='IP' and @class='android.widget.Button']")
   
    
    
    SettingsHomeIcon=(By.XPATH,"//*[@contentDescription='I']")
    IPHomeButton=(By.XPATH,"((//*[contains(@contentDescription,'Settings IP')]/*[@class='android.view.View'])[1]/*[@class='android.widget.Button'])[1]")
    RouterHomeButton=(By.XPATH,"((//*[contains(@contentDescription,'Settings Router')]/*[@class='android.view.View'])[1]/*[@class='android.widget.Button'])[1]")
    Port_S1=(By.XPATH,"//*[@contentDescription='Port S1:']")
    
    Assigned_IPAddress=(By.XPATH,"//*[@contentDescription='Assigned IP Address:' and @class='android.widget.EditText']")
    Assigned_SubnetMask=(By.XPATH,"//*[@contentDescription='Assigned Subnet Mask:' and @class='android.widget.EditText']")
    Assigned_GatewayAddress=(By.XPATH,"//*[@contentDescription='Assigned Gateway IP Addr:' and @class='android.widget.EditText']")
    IPNetwork=(By.XPATH,"//*[@contentDescription='2400']")
    IPNetworkold=(By.XPATH,"//*['@contentDescription='2401']")
    
    
    Assigned_UDP_Port=(By.XPATH,"//*[@contentDescription='Assigned UDP Port:' and @class='android.widget.EditText']")
    
    IP_Save=(By.XPATH,"//*[@contentDescription='Save']")
    IP_Cancel = (By.XPATH, "//*[@contentDescription='Cancel']")
    OK=(By.XPATH,"//*[@contentDescription='OK']")
    
    AppiumServerURL= "http://localhost:4723/wd/hub"
    ErrorMessage=(By.XPATH,"//*[@contentDescription='Enter number between 0 and 65534 for IP Network.']")
    IPPageTextverification=(By.XPATH,"//*[@contentDescription='Settings']")
    IPPage=(By.XPATH,"//*[@class='android.view.View' and ./*[@contentDescription='IP']]")
    editTextFields = (By.TAG_NAME, "EditText")

    












