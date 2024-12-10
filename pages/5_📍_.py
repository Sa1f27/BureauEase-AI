import streamlit as st
import pandas as pd

# Sample Data
data = [
    {"Name": "Meeseva Center", "Purpose": "Citizen services", "Location": "Hyderabad", "Contact": "+91 1100"},
    {"Name": "GHMC Office", "Purpose": "Property tax, grievances", "Location": "Tank Bund Road", "Contact": "+91-40-23225397"},
    {"Name": "TSSPDCL Office", "Purpose": "Electricity services", "Location": "Mint Compound", "Contact": "1912"},
    {"Name": "HMWSSB", "Purpose": "Water supply issues", "Location": "Khairatabad", "Contact": "155313"},
    {"Name": "RTA Office", "Purpose": "Driving licenses", "Location": "Khairatabad", "Contact": "+91-40-23311269"},
    {"Name": "Regional Passport Office", "Purpose": "Passport services", "Location": "Secunderabad", "Contact": "+91-40-27715333"},
    {"Name": "Income Tax Department", "Purpose": "Tax-related inquiries", "Location": "Basheerbagh", "Contact": "+91-40-23425309"},
    {"Name": "Employment Exchange Office", "Purpose": "Job seeker registrations", "Location": "Nampally", "Contact": "+91-40-24651288"},
    {"Name": "Telangana Social Welfare Department", "Purpose": "Welfare schemes", "Location": "Masab Tank", "Contact": "+91-40-23390228"},
    {"Name": "Osmania General Hospital", "Purpose": "Healthcare services", "Location": "Afzal Gunj", "Contact": "+91-40-24600121"},
    {"Name": "NIMS Hospital", "Purpose": "Specialized healthcare", "Location": "Punjagutta", "Contact": "+91-40-23489000"},
    {"Name": "Hyderabad City Police Commissionerate", "Purpose": "Public safety", "Location": "Basheerbagh", "Contact": "+91-40-27852421"},
    {"Name": "Family Court", "Purpose": "Legal family matters", "Location": "Nampally", "Contact": "+91-40-23444789"},
    {"Name": "Consumer Forum", "Purpose": "Consumer disputes", "Location": "Khairatabad", "Contact": "+91-40-23391222"},
    {"Name": "TSRTC Office", "Purpose": "Public transport inquiries", "Location": "Musheerabad", "Contact": "+91-40-27614233"},
    {"Name": "Fire Department", "Purpose": "Fire safety", "Location": "Secunderabad", "Contact": "101"},
    {"Name": "High Court of Telangana", "Purpose": "Judicial services", "Location": "City College Road", "Contact": "+91-40-23446336"},
    {"Name": "Tourism Department Office", "Purpose": "Tourism services", "Location": "Tank Bund Road", "Contact": "+91-40-23455270"},
    {"Name": "South Central Railway Headquarters", "Purpose": "Railway services", "Location": "Rail Nilayam, Secunderabad", "Contact": "+91-40-27820318"},
    {"Name": "General Post Office (GPO)", "Purpose": "Postal services", "Location": "Abids", "Contact": "+91-40-23463980"},
    {"Name": "Telangana State Board of Intermediate Education", "Purpose": "Education services", "Location": "Nampally", "Contact": "+91-40-24603314"},
    {"Name": "Lokayukta Office", "Purpose": "Anti-corruption services", "Location": "Moazzam Jahi Market", "Contact": "+91-40-23240066"},
    {"Name": "All India Radio Hyderabad", "Purpose": "Broadcasting services", "Location": "Gun Foundry", "Contact": "+91-40-23233844"},
    {"Name": "Aadhaar Enrollment Center", "Purpose": "Aadhaar services", "Location": "Hyderabad (various locations)", "Contact": "1947"},
    {"Name": "GHMC Zonal Office", "Purpose": "Local civic issues", "Location": "Banjara Hills", "Contact": "+91-40-23312345"},
    {"Name": "IT Department Office", "Purpose": "Income tax inquiries", "Location": "Aayakar Bhavan, Basheerbagh", "Contact": "+91-40-23425310"},
    {"Name": "Public Library", "Purpose": "Books and research", "Location": "Koti", "Contact": "+91-40-23452347"},
    {"Name": "Disaster Management Office", "Purpose": "Emergency response", "Location": "Masab Tank", "Contact": "+91-40-23234111"},
    {"Name": "Telangana State Election Commission", "Purpose": "Voter services", "Location": "AC Guards", "Contact": "+91-40-23457180"},
    {"Name": "Road Transport Authority (RTA)", "Purpose": "Vehicle registrations", "Location": "Uppal", "Contact": "+91-40-27202345"},
    {"Name": "Cyber Crime Police Station", "Purpose": "Cyber safety", "Location": "Gachibowli", "Contact": "+91-40-27852421"},
    {"Name": "Regional Employment Office", "Purpose": "Skill development and jobs", "Location": "Secunderabad", "Contact": "+91-40-23302288"},
    {"Name": "State Archives", "Purpose": "Historical records", "Location": "Moghalpura", "Contact": "+91-40-24454729"},
    {"Name": "Hyderabad Municipal Corporation", "Purpose": "Local governance", "Location": "Tank Bund", "Contact": "+91-40-23312345"},
    {"Name": "Telangana State Police Headquarters", "Purpose": "Law enforcement", "Location": "Basheerbagh", "Contact": "+91-40-27852421"},
    {"Name": "Hyderabad Traffic Police", "Purpose": "Traffic management", "Location": "Nampally", "Contact": "+91-40-23456789"},
    {"Name": "Telangana Forest Department", "Purpose": "Environmental protection", "Location": "Khairatabad", "Contact": "+91-40-23345678"},
    {"Name": "Hyderabad Fire Station", "Purpose": "Fire emergencies", "Location": "Secunderabad", "Contact": "+91-40-101"},
    {"Name": "Telangana State Archives", "Purpose": "Historical records preservation", "Location": "Moghalpura", "Contact": "+91-40-24454729"},
    {"Name": "Hyderabad Urban Development Authority", "Purpose": "Urban planning and development", "Location": "Jubilee Hills", "Contact": "+91-40-23512345"},
    {"Name": "Telangana State Road Transport Corporation (TSRTC)", "Purpose": "Public transport services", "Location": "Musheerabad", "Contact": "+91-40-27614233"},
    {"Name": "Hyderabad District Collectorate", "Purpose": "Administrative services", "Location": "Nampally", "Contact": "+91-40-24651288"},
    {"Name": "Telangana State Housing Corporation", "Purpose": "Housing schemes and services", "Location": "Banjara Hills", "Contact": "+91-40-23345679"},
    {"Name": "Hyderabad Employment Office", "Purpose": "Job placement services", "Location": "Secunderabad", "Contact": "+91-40-23302288"},
    {"Name": "Telangana Social Welfare Board", "Purpose": "Social welfare programs", "Location": "Masab Tank", "Contact": "+91-40-23390228"},
    {"Name": "Hyderabad Child Welfare Committee", "Purpose": "Child protection services", "Location": "Khairatabad",  "Contact": "+91-40-23456790"},
    {"Name":  "Telangana State Legal Services Authority",  "Purpose":"Legal aid services","Location":"Basheerbagh","Contact":"+91-40-23456780"},
    {"Name":"Hyderabad City Development Authority","Purpose":"City infrastructure development","Location":"Tank Bund","Contact":"+91-40-23456781"},
    {"Name":"Telangana State Pollution Control Board","Purpose":"Environmental regulation","Location":"Koti","Contact":"+91-40-23456782"},
    {"Name":"Hyderabad Public Health Department","Purpose":"Public health services","Location":"Nampally","Contact":"+91-40-23456783"},
    {"Name":"Telangana State Women Commission","Purpose":"Women empowerment services","Location":"Banjara Hills","Contact":"+91-40-23456784"},
    {"Name":"Hyderabad Skill Development Center","Purpose":"Skill training programs","Location":"Secunderabad","Contact":"+91-40-23456785"},
    {"Name":"Telangana State Fisheries Department","Purpose":"Fisheries management","Location":"Khairatabad","Contact":"+91-40-23456786"},
    {"Name":"Hyderabad Animal Husbandry Department","Purpose":"Animal welfare services","Location":"Masab Tank","Contact":"+91-40-23456787"},
    {"Name":"Telangana State Handicrafts Development Corporation","Purpose":"Promotion of handicrafts","Location":"Koti","Contact":"+91-40-23456788"},
    {"Name":"Hyderabad Urban Forestry Department","Purpose":"Urban forestry initiatives","Location":"Jubilee Hills","Contact":"+91-40-23456789"},
    {"Name":"Telangana State Child Rights Protection Commission","Purpose":"Child rights advocacy","Location":"Nampally","Contact":"+91-40-23456790"},
    {"Name":"Hyderabad Disaster Management Authority","Purpose":"Disaster preparedness and response","Location":"Secunderabad","Contact":"+91-40-23456791"},
    {"Name":"Telangana State Sports Authority","Purpose":"Promotion of sports and fitness programs","Location":"Banjara Hills","Contact":"+91-40-23456792"},
    {"Name":"Hyderabad Cultural Centre","Purpose":"Cultural events and activities","Location":"Tank Bund","Contact":"+91-40-23456793"},
    {"Name":"Telangana State Information Commission","Purpose":"Right to Information services","Location":"Khairatabad","Contact":"+91-40-23456794"},
    {"Name":"Hyderabad Youth Welfare Board","Purpose":"Youth development programs","Location":"Masab Tank","Contact":"+91-40-23456795"},
    {"Name":"Telangana State Minority Welfare Department","Purpose":"Minority welfare schemes and services","Location":"Nampally","Contact":"+91+040+23456796"},
    {"Name":"Hyderabad Senior Citizens Forum","Purpose":"Support for senior citizens' issues and needs.","Location ":"Secunderabad "," Contact ":" + 91 - 040 - 23456797"},
    {" Name ":" Telangana State Heritage Conservation Committee "," Purpose ":" Heritage site preservation "," Location ":" Koti "," Contact ":" + 91 - 040 - 23456798"},
    {" Name ":" Hyderabad Traffic Management Center "," Purpose ":" Traffic regulation and safety "," Location ":" Banjara Hills "," Contact ":" + 91 - 040 - 23456799"},
    {" Name ":" Telangana State Civil Supplies Corporation "," Purpose ":" Public distribution system "," Location ":" Jubilee Hills "," Contact ":" + 91 - 040 - 23456800"},
    {" Name ":" Hyderabad Slum Clearance Board "," Purpose ":" Slum rehabilitation and development "," Location ":" Musheerabad "," Contact ":" + 91 - 040 - 23456801"},
    {"Name": "Hyderabad Water Works", "Purpose": "Water supply management", "Location": "Khairatabad", "Contact": "+91-40-23456701"},
    {"Name": "Telangana State Electricity Regulatory Commission", "Purpose": "Electricity regulation", "Location": "Banjara Hills", "Contact": "+91-40-23456702"},
    {"Name": "Hyderabad Municipal Solid Waste Management", "Purpose": "Waste management services", "Location": "Secunderabad", "Contact": "+91-40-23456703"},
    {"Name": "Telangana State Child Development Department", "Purpose": "Child welfare services", "Location": "Nampally", "Contact": "+91-40-23456704"},
    {"Name": "Hyderabad Urban Transport Corporation", "Purpose": "Urban transport planning", "Location": "Jubilee Hills", "Contact": "+91-40-23456705"},
    {"Name": "Telangana State Housing Board", "Purpose": "Housing development schemes", "Location": "Moghalpura", "Contact": "+91-40-23456706"},
    {"Name": "Hyderabad City Heritage Committee", "Purpose": "Heritage conservation efforts", "Location": "Tank Bund", "Contact": "+91-40-23456707"},
    {"Name": "Telangana State Agricultural Department", "Purpose": "Agricultural support services", "Location": "Secunderabad", "Contact": "+91-40-23456708"},
    {"Name": "Hyderabad Skill Development Institute", "Purpose": "Vocational training programs", "Location": "Nampally", "Contact": "+91-40-23456709"},
    {"Name": "Telangana State Women Development Corporation", "Purpose": "Women empowerment initiatives", "Location": "Banjara Hills", "Contact": "+91-40-23456710"},
    {"Name": "Hyderabad Mental Health Center", "Purpose": "Mental health services", "Location": "Khairatabad",  "Contact":"+91-40-23456711"},
    {"Name":"Telangana State Sports Council","Purpose":"Sports promotion and development","Location":"Musheerabad","Contact":"+91-40-23456712"},
    {"Name":"Hyderabad Road Safety Authority","Purpose":"Road safety awareness","Location":"Secunderabad","Contact":"+91-40-23456713"},
    {"Name":"Telangana State Fisheries Department","Purpose":"Fisheries management and support","Location":"Koti","Contact":"+91-40-23456714"},
    {"Name":"Hyderabad Urban Planning Office","Purpose":"Urban development planning","Location":"Jubilee Hills","Contact":"+91-40-23456715"},
    {"Name":"Telangana State Fire Services","Purpose":"Fire safety and prevention","Location":"Tank Bund","Contact":"+91-40-101"},
    {"Name":"Hyderabad Consumer Protection Council","Purpose":"Consumer rights advocacy","Location":"Nampally","Contact":"+91-40-23456716"},
    {"Name":"Telangana State Environmental Protection Agency","Purpose":"Environmental conservation efforts","Location":"Basheerbagh","Contact":"+91-40-23456717"},
    {"Name":"Hyderabad Public Works Department","Purpose":"Infrastructure development and maintenance","Location":"Khairatabad","Contact":"+91-40-23456718"},
    {"Name":"Telangana State Youth Affairs Department","Purpose":"Youth engagement programs","Location":"Secunderabad","Contact":"+91-40-23456719"},
    {"Name":"Hyderabad Cultural Heritage Board","Purpose":"Cultural heritage preservation","Location":"Banjara Hills","Contact":"+91-40-23456720"},
    {"Name":"Telangana State Disaster Relief Fund Office","Purpose":"Disaster relief coordination","Location":"Masab Tank","Contact":"+91-40-23456721"},
]

# Combine the original data with the new additional data
services_df = pd.DataFrame(data)

def display_services_list(filtered_df):
    """
    Display services in a grid format with each location in a box and emojis.
    """
    # Check for an empty DataFrame
    if filtered_df.empty:
        st.warning("No services to display. Please refine your filters.")
        return

    # Check for required columns
    required_columns = ['Location', 'Name', 'Purpose', 'Contact']
    missing_columns = [col for col in required_columns if col not in filtered_df.columns]
    if missing_columns:
        st.error(f"Missing required columns in the data: {', '.join(missing_columns)}")
        return

    # Pagination setup
    items_per_page = 10
    total_items = len(filtered_df)
    total_pages = (total_items + items_per_page - 1) // items_per_page

    if total_pages == 0:
        total_pages = 1  # Ensure at least one page is shown if there are no items

    current_page = st.number_input(
        "Page",
        min_value=1,
        max_value=total_pages,
        value=1,
        step=1
    )

    # Calculate start and end indices
    start_idx = (current_page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, total_items)

    # Slice the DataFrame for the current page
    page_df = filtered_df.iloc[start_idx:end_idx]

    # Display services in a grid format
    columns = 3  # Number of columns in the grid

    st.write("## Services List")

    if page_df.empty:
        st.warning("No services available on this page.")
        return

    for idx in range(0, len(page_df), columns):
        cols = st.columns(columns)
        for col, (_, row) in zip(cols, page_df.iloc[idx:idx+columns].iterrows()):
            with col:
                st.markdown(
                    f"<div style='border: 2px solid #E8E8E8; border-radius: 8px; padding: 10px; margin: 5px;'>"
                    f"<h4>📍 {row['Location']}</h4>"
                    f"<p><strong>Name:</strong> {row['Name']}</p>"
                    f"<p><strong>Purpose:</strong> {row['Purpose']}</p>"
                    f"<p><strong>Contact:</strong> 📞 {row['Contact']}</p>"
                    f"</div>",
                    unsafe_allow_html=True
                )

    # Page info
    st.caption(f"Showing {start_idx + 1}-{end_idx} of {total_items} services")


def main():
    # App title and styling
    st.set_page_config(page_title="Hyderabad Services Finder", page_icon="🏛️")
    st.title("🏛️ Hyderabad Services Finder")

    # Convert Purpose column to string to avoid sorting issues
    services_df['Purpose'] = services_df['Purpose'].astype(str)

    # Purpose filter
    purpose_filter = st.selectbox(
        "Filter by Service Purpose:", ["All"] + sorted(services_df["Purpose"].unique())
    )

    
    filtered_df = services_df

    # Apply purpose filter
    if purpose_filter != "All":
        filtered_df = filtered_df[filtered_df["Purpose"] == purpose_filter]

    # Check if any services match the filters
    if filtered_df.empty:
        st.warning("No services found matching your search criteria.")
    else:
        # Display filtered services
        display_services_list(filtered_df)

if __name__ == "__main__":
    main()