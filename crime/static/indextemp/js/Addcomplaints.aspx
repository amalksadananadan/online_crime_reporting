<%@ Page Language="C#" AutoEventWireup="true" MasterPageFile="~/Visitor/visitormaster2.master" CodeFile="Addcomplaints.aspx.cs" Inherits="Visitor_Addcomplaints" %>

<%@ Register assembly="AjaxControlToolkit" namespace="AjaxControlToolkit" tagprefix="cc1" %>


    <%--<style type="text/css">
    
        .auto-style1
        {
            width: 100%;
        }
        .auto-style2
        {
            height: 23px;
        }
        .auto-style3
        {
            height: 26px;
        }
        .auto-style4
        {
            height: 30px;
        }
        .auto-style6
        {
            width: 432px;
        }
        .auto-style7
        {
            height: 30px;
            width: 432px;
        }
        .auto-style8
        {
            height: 26px;
            width: 432px;
        }
        .auto-style10
        {
            height: 23px;
            width: 432px;
        }
        .auto-style12
        {
            height: 25px;
        }
        .auto-style13
        {
            height: 25px;
            width: 432px;
        }
        .auto-style14
        {
            height: 59px;
        }
        .auto-style15
        {
            width: 432px;
            height: 59px;
        }
    </style>
    <link href="../Officer/StyleSheet.css" rel="stylesheet" type="text/css" />
    <link href="../Admin/StyleSheet.css" rel="stylesheet" type="text/css" />
</head>
<body>--%>
    <asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
    <form id="form1" runat="server">
        <table class="auto-style1">
            <tr>
                <td class="heading" colspan="3">ADD COMPLAINTS<cc1:ToolkitScriptManager ID="ToolkitScriptManager1" runat="server">
                    </cc1:ToolkitScriptManager>
                </td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td class="auto-style6">Case Type</td>
                <td>
                    <asp:DropDownList ID="DropDownList1" runat="server">
                    </asp:DropDownList>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ControlToValidate="DropDownList1" ErrorMessage="Please select case type" ForeColor="Red"></asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td class="auto-style4"></td>
                <td class="auto-style7">District</td>
                <td class="auto-style4">
                    <asp:DropDownList ID="DropDownList2" runat="server">
                        <asp:ListItem Selected="True">Kasaragod</asp:ListItem>
                        <asp:ListItem>Kannur</asp:ListItem>
                        <asp:ListItem>wayanad</asp:ListItem>
                        <asp:ListItem>Kozhikode</asp:ListItem>
                        <asp:ListItem>Malappuram</asp:ListItem>
                        <asp:ListItem>Palakkad</asp:ListItem>
                        <asp:ListItem>Thrissur</asp:ListItem>
                        <asp:ListItem>Ernakulam</asp:ListItem>
                        <asp:ListItem>Idukki</asp:ListItem>
                        <asp:ListItem>Kottayam</asp:ListItem>
                        <asp:ListItem>Alappuzha</asp:ListItem>
                        <asp:ListItem>Pathanamthitta</asp:ListItem>
                        <asp:ListItem>Kollam</asp:ListItem>
                        <asp:ListItem>Thiruvananthapuram</asp:ListItem>
                    </asp:DropDownList>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator3" runat="server" ControlToValidate="DropDownList2" ErrorMessage="Please select the district" ForeColor="Red"></asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td class="auto-style3">&nbsp;</td>
                <td class="auto-style8">Case City</td>
                <td class="auto-style3">
                    <asp:TextBox ID="txtcity" runat="server" CssClass="textbox"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator4" runat="server" ControlToValidate="txtcity" ErrorMessage="Please enter the case city" ForeColor="Red"></asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td class="auto-style14"></td>
                <td class="auto-style15">Case Details</td>
                <td class="auto-style14">
                    <asp:TextBox ID="txtdetails" runat="server" CssClass="textbox"></asp:TextBox>
                    <cc1:FilteredTextBoxExtender ID="txtdetails_FilteredTextBoxExtender" runat="server" Enabled="True" FilterType="Custom, UppercaseLetters, LowercaseLetters" InvalidChars="." TargetControlID="txtdetails">
                    </cc1:FilteredTextBoxExtender>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator5" runat="server" ControlToValidate="txtdetails" ErrorMessage="Please enter case details" ForeColor="Red"></asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td class="auto-style12"></td>
                <td class="auto-style13">Case Date</td>
                <td class="auto-style12">
                    <asp:TextBox ID="txtdate" runat="server" CssClass="textbox" TextMode="Date"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator8" runat="server" ControlToValidate="txtdate" ErrorMessage="Please enter the date" ForeColor="Red"></asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td class="auto-style2"></td>
                <td class="auto-style10">Case Time</td>
                <td class="auto-style2">
                    <asp:TextBox ID="txttime" runat="server" CssClass="textbox"></asp:TextBox>
                    <cc1:FilteredTextBoxExtender ID="txttime_FilteredTextBoxExtender" runat="server" Enabled="True" FilterType="Numbers" TargetControlID="txttime">
                    </cc1:FilteredTextBoxExtender>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator9" runat="server" ControlToValidate="txttime" ErrorMessage="Please enter the case time" ForeColor="Red"></asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td class="auto-style2"></td>
                <td class="auto-style10">
                    <asp:Button ID="Button1" runat="server" CssClass="button" Text="ADD" OnClick="Button1_Click"/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <asp:Button ID="Button2" runat="server" CssClass="button" Text="CLEAR" OnClick="Button2_Click1" />
                </td>
                <td class="auto-style2"></td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td class="auto-style6">&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
        </table>
    </form>
</asp:Content>
