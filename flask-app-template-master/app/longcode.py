def calculate_footprint(data, electricity,frequency):

    elec = electricity
    factors = {"Car":0.21, "Bike":0.05, "Cycle":0, "Train":0.04, "Bus":0.05, "Foot":0}
    freq_mult = {"Quarterly":4,"Monthly":1,"Annually":12}
    freq = freq_mult.get(frequency)
    transport_emission=0
    electricity_emission_factor = 0.82
    for d in data:
        mot,dist = d[0],d[1]
        transport_emission_factor = factors.get(mot)
        transport_emission += transport_emission_factor*dist
        ###print(transport_emission_factor,transport_emission) debugging
    electricity_emission = elec * electricity_emission_factor
    total_emission = transport_emission + electricity_emission
    total_emission *= freq
    suggestions = provide_suggestions(transport_emission, electricity_emission)

    return [round(total_emission,2), suggestions, transport_emission, electricity_emission]


# providing user suggestions+
def provide_suggestions(transport_emission, electricity_emission):
    suggestions = []

    # Suggestion for Transport
    if transport_emission > 5:  # Example threshold for transport emissions
        suggestions.append("Consider carpooling, using public transport, or biking more often.")

    # Suggestion for Electricity Usage
    if electricity_emission > 100:  # Example threshold for electricity usage
        suggestions.append("Switch to energy-efficient appliances or reduce usage during peak hours.")

    return "\n".join(suggestions) if suggestions else "Your carbon footprint is already quite low! Keep it up!"

