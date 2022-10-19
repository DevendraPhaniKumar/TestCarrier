from selenium.webdriver.common.by import By

class LoginPageLocatars(object):
    EMAIL = (By.ID, "nameInput")
    PASSWORD = (By.ID, "pass")
    SUBMIT = (By.ID, "submit")
    Bodytext = (By.XPATH, '//*[@id="MainBarTR"]/td[5]/div/img')
    logout = (By.XPATH, '//*[@title="System Menu"]')
    LogoutLink=(By.XPATH,'//*[@id="main_logout"]')
    

class ConfigurePage(object):
    checkboxcollapse = (By.XPATH, '//*[@id="paddedDiv"]/table[5]/tbody/tr[2]/td/div/img')
    actionframe='actionContent'
    
    BacNetIPConnection=(By.ID,'xp0connectionsTable')
    stopButtonOrStart=(By.XPATH,'//*[@id="paddedDiv"]/div[2]/div[1]/table/tbody/tr[2]/td/span[2]/span[2]/span')
    iPAddressField=(By.XPATH,'//*[@id="bacnetip"]/span[2]')
    subneMask=(By.XPATH, '//*[@id="bacnetip"]/span[3]')
    iPAddressFieldd=(By.ID,'undefined')
    bacnetIPPanel=(By.XPATH,'//*[@id="bacnetip"]')
    AcceptButton=(By.XPATH,'//*[@id="acceptSpan"]/span[1]')
    cancelButton=(By.XPATH,'//*[@id="acceptSpan"]/span[2]')
    ApplyButton=(By.XPATH,'//*[@id="acceptSpan"]/span[3]')
    sourcePath=(By.XPATH,".//*[@id='sourcePath']")
    expandCategories=(By.XPATH,"//div[@id='configTree_19d']/div/img")
    

class GeoPageLocators(object):
    pageString=(By.ID,'pathSpace')

class Downloadpage(object):
    addButton=(By.XPATH,"//div[text()='Add...']")
    startButton=(By.XPATH,"//div[text()='Start']")
    addButtonOnPopup=(By.XPATH,"//div[text()='Add']")
    selectAllCheckBox=(By.XPATH,"//span[text()='Select all']")
        
class WebCTRLPageLocators(object):
    ActionButtonSpan=(By.ID, "actButtonSpan")
    ActionButtonContainer=(By.ID,"facetButtonContainer")
    DivOfActionButton = (By.TAG_NAME, "div")
    SpanOfActionButton = (By.TAG_NAME, "span")
    DropDownArrow=(By.TAG_NAME, "img")    
    DriverDropDown=(By.XPATH,'//*[@id="paddedDiv"]/table[2]/tbody/tr[2]/td/div/table[1]')
    TableIframe=(By.ID,'actioncategories')
    PopupTable=(By.XPATH, '//*[@id="container"]')
    DivOfActionButton2 = (By.TAG_NAME, "nobr")
    GeoTreeHead=(By.ID,'geoTree_2')
    NetTreeHead=(By.ID,'netTree_166')
    DropDownMenu=(By.CLASS_NAME,'menuSection barBg')
    IconListId=(By.CLASS_NAME, 'buttonSection barBg')
    ActionBar=(By.XPATH,'//*[@id="actionBar"]')
    ActionBarTable=(By.TAG_NAME,"td")
    ActionBarMain=(By.XPATH, '//*[@id="MainBarTR"]')
    ActionContainer=(By.XPATH, '//*[@id="ActionContentContainer"]')
    TimeLapseWindowTable=(By.ID, 'tmCalendarModal')
    NetworkTree=(By.NAME,'navTableFrame')
    ScrollBar=(By.ID,'navVbar')
    AddButton=(By.XPATH,'//*[@id="paddedDiv"]/table[2]/tbody/tr[2]/td/div/table[2]/tbody/tr/td[1]/span/span')
    ContinueButton=(By.XPATH,'//*[@id="addform"]/table/tbody/tr[4]/td/span')
    MenuTable=(By.XPATH,'//*[@id="menutable"]/tbody')
    Configure=(By.XPATH, '//*[@id="mnuConfigureText"]')
    PathElement=(By.XPATH,".//*[@id='sourcePath']")
    Upload_Sucess=(By.XPATH,'//*[@id="paddedDiv"]/div')
    ConfigTree=(By.CSS_SELECTOR,"[title='System Configuration']")
    securityPassword=(By.XPATH,'//input[@type="password"]')
    okButton=(By.XPATH,"//div[text()='OK']")
    cance_Button=(By.XPATH,"//div[text()='Cancel']")
    simulateButton=(By.XPATH,"//span[@title='Simulate receipt of a return to normal']")
    simulateButton2=(By.XPATH,"//span[@title='Simulate receipt of an alarm']")
    landscapereportradioButton=(By.XPATH,'//*[@id="paddedDiv"]/div[3]/span[2]/table[1]/tbody/tr/td[6]/img')
    runButton=(By.XPATH,"//div[text()='Run']")
    reasonText=(By.XPATH,'//*[@id="dataTable"]/tbody/tr/td[11]/div')
    
    commentBox=(By.XPATH,'//a[@id="ReasonPrimitive"]//textarea')
    checkboxAlarm=(By.XPATH,"//div[@id='eventList']//span[1]//img[1]")
    acknowledgeButton=(By.XPATH,"//span[@title='Acknowledge the selected alarm']")
    forceNormalButton=(By.XPATH,"//span[@title='Force a return to normal for the selected alarm']")
    deleteButton=(By.XPATH,"//span[@title='Delete the selected alarm']")
    coptoclipboardButton=(By.XPATH,"//span[@title='Copy to the clipboard']")
    
    
    missingReason=(By.XPATH,'//div[@id="missingReasonError"]/span')
    invalidPassword=(By.XPATH,'//div[@id="invalidPasswordError"]/span[1]')
    invalidPassword1=(By.XPATH,'//div[@id="invalidPasswordError"]/span[2]')
    missingPassword=(By.XPATH,'//div[@id="missingPasswordError"]/span')
    tooLongReason=(By.XPATH,'//div[@id="tooLongReasonError"]/span[1]')
    
    statusOfAlarm2=(By.XPATH,"//div[@id='eventList']//div[2]//span[4]/div")
    statusOfAlarm=(By.XPATH,"//div[@id='eventList']//span[4]/div")
    rightMenu_iFrame="rightMenuiframe"
    faceContentIframe="facetContent"
    networkIframe="navTableFrame"
    navContent_Frame="navContent"
    menuFrame="menu1"
    actionCategoriesFrame='actioncategories'
    menuTableid=(By.ID,"menutable")
    actionframe='actionContent'
    actionInstancesFrame='actioninstances'
    
    
    alarmGeneratorON_OF = (By.XPATH, '//*[@id="paddedDiv"]/a[2]')
    onLink=(By.XPATH,'//*[@id="paddedDiv"]/span[4]/div[2]')
    offLink=(By.XPATH,'//*[@id="paddedDiv"]/span[4]/div[1]')
    systemLevelAlarms=(By.XPATH,'//*[@id="MainBarTR"]/td[4]/img[3]')
    evenList=(By.ID,'eventList')
    listCountTag=(By.CLASS_NAME,'WidgetEventRecord-base')
    alarmEnabled_noneRadioButton=(By.XPATH,'//*[@id="AlarmOptionsLeftColumn"]/div[2]/img[3]')
    selectCategoryDropdown=(By.XPATH,'//*[@id="AlarmInstructions"]/span[1]/a/span[1]')
    selectCategoryList=(By.XPATH,'//*[@id="cjOuter"]/span')
    changeButton=(By.XPATH,'//*[@id="AlarmInstructions"]/span[2]/span/span')
    securityWindowPassword=(By.XPATH,'/html/body/table/tbody/tr[1]/td[2]/input')
    securityWindowtextArea=(By.XPATH,'//*[@id="ReasonPrimitive"]/textarea')
    securityWindowOkButton=(By.XPATH,'/html/body/table/tbody/tr[3]/td/span[1]')
    dropDownList=(By.XPATH,'//*[@id="scrollContent"]/span')
    
    

class AlarmsPage(object):
    SelectedCount = (By.XPATH, '//*[@id="SelectionCount"]')
    Schedules = (By.XPATH, '//*[@id="paddedDiv"]/table/tbody/tr[1]/td[2]/span')
    Privileges = (By.XPATH, '//*[@id="paddedDiv"]/table/tbody/tr[2]/td[2]')
    GoButton = (By.XPATH, '//*[@id="AlarmHeaderRight"]/div[3]/span/span/div')
    dropDown = (By.XPATH, '//*[@id="bodyTable"]/tbody/tr[6]/td[5]/img')
    advanced=(By.XPATH,"//div[text()='Advanced']")

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
    

class ACT(object):
    '''
    Configuration & Design page locators
    '''
    configDesignBtn = (By.XPATH,'//*[@id="configure"]')
    uploadBtn = (By.XPATH,'//*[@id="show_upload_frame"]')
    uploadXBtn = (By.XPATH,'//*[@id="upload_close"]')
    loadExistingFileBtn = (By.XPATH,'//*[@id="btn_upload"]')
    autoDetectBtn = (By.XPATH, '//*[@id="btn_detect"]')
    table = (By.XPATH,'//*[@id="result"]/table/tbody')
    row = (By.XPATH,'//*[@id="result"]/table/tbody/tr')
    columns = (By.XPATH,'')
    
    '''
    Buttons
    '''
    okBtn = (By.XPATH,'//*[@id="submitAutoDetect"]')
    resetBtn = (By.XPATH,'//*[@id="resetAutoDetect"]')
    
    '''
    AutoDetectDevices Parameters
    '''
    ahuRefLbl = (By.XPATH,'//*[@id="form-horizontal-2"]/div[2]/label')
    ahuRefParam = (By.XPATH,'//*[@id="focusedInput_9"]')
    vavRefLbl = (By.XPATH,'//*[@id="form-horizontal-2"]/div[3]/label')
    vavRefParam = (By.XPATH,'//*[@id="focusedInput_10"]')
    
    damperPosOverrideLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[1]/label')
    damperPosOverride = (By.XPATH,'//*[@id="focusedInput_12"]')
    damperPosOverEnablelableLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[2]/label')
    damperPosOverEnablelable = (By.XPATH,'//*[@id="focusedInput_13"]')
    rhPosOverrideLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[3]/label')
    rhPosOverrideParam = (By.XPATH,'//*[@id="focusedInput_14"]')
    rhPosOverEnableLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[4]/label')
    rhPosOverEnableParam = (By.XPATH,'//*[@id="focusedInput_15"]')
    damperPosCmdTrndLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[5]/label')
    damperPosCmdTrndParam = (By.XPATH,'//*[@id="focusedInput_16"]')
    damperPosFdbkTrnd =  (By.XPATH,'//*[@id="form-horizontal-3"]/div[6]/label')
    damperPosFdbkTrndParam =  (By.XPATH,'//*[@id="focusedInput_1"]')
    rhPosCmdTrndLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[7]/label')
    rhPosCmdTrndParam = (By.XPATH,'//*[@id="focusedInput_17"]')
    vavFlowTrndLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[9]/label')
    vavFlowTrndParam = (By.XPATH,'//*[@id="focusedInput_2"]')
    vavDisTempTrndLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[10]/label')
    vavDisTempTrndParam = (By.XPATH,'//*[@id="focusedInput_3"]')
    ahuSplyTmpTrndLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[11]/label')
    ahusplyTmpTndParam = (By.XPATH,'//*[@id="focusedInput_4"]')
    ahufanStsLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[15]/label')
    ahufanStsParam = (By.XPATH,'//*[@id="focusedInput_8"]')
    vavMinAirFlowLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[16]/label')
    vavMinAirFlowParam = (By.XPATH,'//*[@id="focusedInput_19"]')
    vavMaxAirFlowLbl = (By.XPATH,'//*[@id="form-horizontal-3"]/div[17]/label')
    vavMaxAirFlowParam = (By.XPATH,'//*[@id="focusedInput_20"]')
    










class EndToEndGraphicsPage(object):
    OnText=(By.XPATH,'//*[@id="region17"]/span/div/div[3]/table/tbody/tr/td/span/span/div')
    ResolveButton=(By.XPATH,"//*[@id='ch_common_header']/span[1]/span/div")
    FailedText=(By.XPATH, "//*[@id='inline_text7']")
    smokeText=(By.XPATH, "//*[@id='region23']/table/tbody/tr/td/table/tbody/tr/td/span")
    
    












