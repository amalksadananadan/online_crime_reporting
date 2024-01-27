using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Visitor_Addcomplaints : System.Web.UI.Page
{
    criminal obj = new criminal();
    protected void Page_Load(object sender, EventArgs e)
    {
        if (!IsPostBack)
        {
            Session["uname"] = "greeshma";
            obj.FillDropDownList("ctype", "ctypeid", "casetype", "", DropDownList1);
        }
    }
  
    protected void Button1_Click(object sender, EventArgs e)
    {
        obj.writedata("insert into complaints values(" + DropDownList1.SelectedValue + ",'" + DropDownList2.SelectedItem.Text + "','" + txtcity.Text + "','" + txtdetails.Text + "','" + txtdate.Text + "','" + txttime.Text + "','" + (String)Session["uname"] + "','pending')");
        Response.Write(obj.MessageBox("data saved successfully"));
        obj.readdata("select max(cmpid) as cmpid from complaints");
        if (obj.dr.Read())
        {
            Session["cmpid"] = obj.dr["cmpid"].ToString();
        }
        if (DropDownList1.SelectedItem.Text == "theft")
        {
            Response.Redirect("Theftcomplaint.aspx");
        }
        else if (DropDownList1.SelectedItem.Text == "missing")
        {
            Response.Redirect("Missingcase.aspx");
        }
    }
    protected void Button2_Click1(object sender, EventArgs e)
    {
        txtcity.Text = " ";
        txtdetails.Text = " ";
        txtdate.Text = " ";
        txttime.Text = " ";
    }
}