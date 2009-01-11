"""
"""
from __future__ import absolute_import

import math as _math
from .codata import physical_constants as _pc
from quantities.quantity import Quantity
from quantities.uncertainquantity import UncertainQuantity

def _cd(name):
    entry = _pc[name]
    if entry['precision']:
        return UncertainQuantity(
            entry['value'], entry['units'], entry['precision']
        )
    else:
        return Quantity(entry['value'], entry['units'])

#mathematical constants
pi = _math.pi
golden = golden_ratio = (1 + _math.sqrt(5)) / 2

#SI prefixes
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deka = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21

#binary prefixes
kibi = 2**10
mebi = 2**20
gibi = 2**30
tebi = 2**40
pebi = 2**50
exbi = 2**60
zebi = 2**70
yobi = 2**80

#physical constants
d_220 = a_Si_220 = silicon_220_lattice_spacing = \
    _cd('{220} lattice spacing of silicon')
alpha_particle_electron_mass_ratio = \
    _cd('alpha particle-electron mass ratio')
m_alpha = alpha_particle_mass = \
    _cd('alpha particle mass')
alpha_particle_mass_energy_equivalent = \
    _cd('alpha particle mass energy equivalent')
alpha_particle_mass_energy_equivalent_in_MeV = \
    _cd('alpha particle mass energy equivalent in MeV')
alpha_particle_mass_in_u = \
    _cd('alpha particle mass in u')
alpha_particle_molar_mass = \
    _cd('alpha particle molar mass')
alpha_particle_proton_mass_ratio = \
    _cd('alpha particle-proton mass ratio')
Angstrom_star = \
    _cd('Angstrom star')
amu = atomic_mass_constant = \
    _cd('atomic mass constant')
atomic_mass_constant_energy_equivalent = \
    _cd('atomic mass constant energy equivalent')
atomic_mass_constant_energy_equivalent_in_MeV = \
    _cd('atomic mass constant energy equivalent in MeV')
atomic_mass_unit_electron_volt_relationship = \
    _cd('atomic mass unit-electron volt relationship')
atomic_mass_unit_hartree_relationship = \
    _cd('atomic mass unit-hartree relationship')
atomic_mass_unit_hertz_relationship = \
    _cd('atomic mass unit-hertz relationship')
atomic_mass_unit_inverse_meter_relationship = \
    _cd('atomic mass unit-inverse meter relationship')
atomic_mass_unit_joule_relationship = \
    _cd('atomic mass unit-joule relationship')
atomic_mass_unit_kelvin_relationship = \
    _cd('atomic mass unit-kelvin relationship')
atomic_mass_unit_kilogram_relationship = \
    _cd('atomic mass unit-kilogram relationship')
atomic_unit_of_1st_hyperpolarizablity = \
    _cd('atomic unit of 1st hyperpolarizablity')
atomic_unit_of_2nd_hyperpolarizablity = \
    _cd('atomic unit of 2nd hyperpolarizablity')
hbar = atomic_unit_of_action = \
    _cd('atomic unit of action')
atomic_unit_of_charge = \
    _cd('atomic unit of charge')
atomic_unit_of_charge_density = \
    _cd('atomic unit of charge density')
atomic_unit_of_current = \
    _cd('atomic unit of current')
atomic_unit_of_electric_dipole_moment = \
    _cd('atomic unit of electric dipole moment')
atomic_unit_of_electric_field = \
    _cd('atomic unit of electric field')
atomic_unit_of_electric_field_gradient = \
    _cd('atomic unit of electric field gradient')
atomic_unit_of_electric_polarizablity = \
    _cd('atomic unit of electric polarizablity')
atomic_unit_of_electric_potential = \
    _cd('atomic unit of electric potential')
atomic_unit_of_electric_quadrupole_moment = \
    _cd('atomic unit of electric quadrupole moment')
atomic_unit_of_energy = \
    _cd('atomic unit of energy')
atomic_unit_of_force = \
    _cd('atomic unit of force')
a_0 = atomic_unit_of_length = \
    _cd('atomic unit of length')
atomic_unit_of_magnetic_dipole_moment = \
    _cd('atomic unit of magnetic dipole moment')
atomic_unit_of_magnetic_flux_density = \
    _cd('atomic unit of magnetic flux density')
atomic_unit_of_magnetizability = \
    _cd('atomic unit of magnetizability')
m_e = atomic_unit_of_mass = \
    _cd('atomic unit of mass')
atomic_unit_of_momentum = \
    _cd('atomic unit of momentum')
atomic_unit_of_permittivity = \
    _cd('atomic unit of permittivity')
atomic_unit_of_time = \
    _cd('atomic unit of time')
atomic_unit_of_velocity = \
    _cd('atomic unit of velocity')
N_A = L = Avogadro_constant = \
    _cd('Avogadro constant')
mu_B = Bohr_magneton = \
    _cd('Bohr magneton')
Bohr_magneton_in_eV_per_T = \
    _cd('Bohr magneton in eV/T')
Bohr_magneton_in_Hz_per_T = \
    _cd('Bohr magneton in Hz/T')
Bohr_magneton_in_inverse_meters_per_tesla = \
    _cd('Bohr magneton in inverse meters per tesla')
Bohr_magneton_in_K_per_T = \
    _cd('Bohr magneton in K/T')
a_0 = Bohr_radius = \
    _cd('Bohr radius')
k = Boltzmann_constant = \
    _cd('Boltzmann constant')
Boltzmann_constant_in_eV_per_K = \
    _cd('Boltzmann constant in eV/K')
Boltzmann_constant_in_Hz_per_K = \
    _cd('Boltzmann constant in Hz/K')
Boltzmann_constant_in_inverse_meters_per_kelvin = \
    _cd('Boltzmann constant in inverse meters per kelvin')
Z_0 = characteristic_impedance_of_vacuum = \
    _cd('characteristic impedance of vacuum')
r_e = classical_electron_radius = \
    _cd('classical electron radius')
lambda_C = Compton_wavelength = \
    _cd('Compton wavelength')
Compton_wavelength_over_2_pi = \
    _cd('Compton wavelength over 2 pi')
G_0 = conductance_quantum = \
    _cd('conductance quantum')
K_J90 = conventional_value_of_Josephson_constant = \
    _cd('conventional value of Josephson constant')
R_K90 = conventional_value_of_von_Klitzing_constant = \
    _cd('conventional value of von Klitzing constant')
Cu_x_unit = \
    _cd('Cu x unit')
deuteron_electron_magnetic_moment_ratio = \
    _cd('deuteron-electron magnetic moment ratio')
deuteron_electron_mass_ratio = \
    _cd('deuteron-electron mass ratio')
g_d = deuteron_g_factor = \
    _cd('deuteron g factor')
mu_d = deuteron_magnetic_moment = \
    _cd('deuteron magnetic moment')
deuteron_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('deuteron magnetic moment to Bohr magneton ratio')
deuteron_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('deuteron magnetic moment to nuclear magneton ratio')
m_d = deuteron_mass = \
    _cd('deuteron mass')
deuteron_mass_energy_equivalent = \
    _cd('deuteron mass energy equivalent')
deuteron_mass_energy_equivalent_in_MeV = \
    _cd('deuteron mass energy equivalent in MeV')
deuteron_mass_in_u = \
    _cd('deuteron mass in u')
deuteron_molar_mass = \
    _cd('deuteron molar mass')
deuteron_neutron_magnetic_moment_ratio = \
    _cd('deuteron-neutron magnetic moment ratio')
deuteron_proton_magnetic_moment_ratio = \
    _cd('deuteron-proton magnetic moment ratio')
deuteron_proton_mass_ratio = \
    _cd('deuteron-proton mass ratio')
R_d = deuteron_rms_charge_radius = \
    _cd('deuteron rms charge radius')
vacuum_permitivity = epsilon_0 = electric_constant = \
    _cd('electric constant')
electron_charge_to_mass_quotient = \
    _cd('electron charge to mass quotient')
electron_deuteron_magnetic_moment_ratio = \
    _cd('electron-deuteron magnetic moment ratio')
electron_deuteron_mass_ratio = \
    _cd('electron-deuteron mass ratio')
g_e = electron_g_factor = \
    _cd('electron g factor')
gamma_e = electron_gyromagnetic_ratio = \
    _cd('electron gyromagnetic ratio')
electron_gyromagnetic_ratio_over_2_pi = \
    _cd('electron gyromagnetic ratio over 2 pi')
mu_e = electron_magnetic_moment = \
    _cd('electron magnetic moment')
a_e = electron_magnetic_moment_anomaly = \
    _cd('electron magnetic moment anomaly')
electron_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('electron magnetic moment to Bohr magneton ratio')
electron_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('electron magnetic moment to nuclear magneton ratio')
m_e = electron_mass = \
    _cd('electron mass')
electron_mass_energy_equivalent = \
    _cd('electron mass energy equivalent')
electron_mass_energy_equivalent_in_MeV = \
    _cd('electron mass energy equivalent in MeV')
electron_mass_in_u = \
    _cd('electron mass in u')
electron_molar_mass = \
    _cd('electron molar mass')
electron_muon_magnetic_moment_ratio = \
    _cd('electron-muon magnetic moment ratio')
electron_muon_mass_ratio = \
    _cd('electron-muon mass ratio')
electron_neutron_magnetic_moment_ratio = \
    _cd('electron-neutron magnetic moment ratio')
electron_neutron_mass_ratio = \
    _cd('electron-neutron mass ratio')
electron_proton_magnetic_moment_ratio = \
    _cd('electron-proton magnetic moment ratio')
electron_proton_mass_ratio = \
    _cd('electron-proton mass ratio')
electron_tau_mass_ratio = \
    _cd('electron-tau mass ratio')
electron_to_alpha_particle_mass_ratio = \
    _cd('electron to alpha particle mass ratio')
electron_to_shielded_helion_magnetic_moment_ratio = \
    _cd('electron to shielded helion magnetic moment ratio')
electron_to_shielded_proton_magnetic_moment_ratio = \
    _cd('electron to shielded proton magnetic moment ratio')
eV = electron_volt = \
    _cd('electron volt')
electron_volt_atomic_mass_unit_relationship = \
    _cd('electron volt-atomic mass unit relationship')
electron_volt_hartree_relationship = \
    _cd('electron volt-hartree relationship')
electron_volt_hertz_relationship = \
    _cd('electron volt-hertz relationship')
electron_volt_inverse_meter_relationship = \
    _cd('electron volt-inverse meter relationship')
electron_volt_joule_relationship = \
    _cd('electron volt-joule relationship')
electron_volt_kelvin_relationship = \
    _cd('electron volt-kelvin relationship')
electron_volt_kilogram_relationship = \
    _cd('electron volt-kilogram relationship')
e = elementary_charge = \
    _cd('elementary charge')
elementary_charge_over_h = \
    _cd('elementary charge over h')
F = Faraday_constant = \
    _cd('Faraday constant')
#F_star = Faraday_constant_for_conventional_electric_current = \
#    _cd('Faraday constant for conventional electric current') what is a unit of C_90?
Fermi_coupling_constant = \
    _cd('Fermi coupling constant')
alpha = fine_structure_constant = \
    _cd('fine-structure constant')
c_1 = first_radiation_constant = \
    _cd('first radiation constant')
c_1L = first_radiation_constant_for_spectral_radiance = \
    _cd('first radiation constant for spectral radiance')
hartree_atomic_mass_unit_relationship = \
    _cd('hartree-atomic mass unit relationship')
hartree_electron_volt_relationship = \
    _cd('hartree-electron volt relationship')
E_h = Hartree_energy = \
    _cd('Hartree energy')
Hartree_energy_in_eV = \
    _cd('Hartree energy in eV')
hartree_hertz_relationship = \
    _cd('hartree-hertz relationship')
hartree_inverse_meter_relationship = \
    _cd('hartree-inverse meter relationship')
hartree_joule_relationship = \
    _cd('hartree-joule relationship')
hartree_kelvin_relationship = \
    _cd('hartree-kelvin relationship')
hartree_kilogram_relationship = \
    _cd('hartree-kilogram relationship')
helion_electron_mass_ratio = \
    _cd('helion-electron mass ratio')
m_h = helion_mass = \
    _cd('helion mass')
helion_mass_energy_equivalent = \
    _cd('helion mass energy equivalent')
helion_mass_energy_equivalent_in_MeV = \
    _cd('helion mass energy equivalent in MeV')
helion_mass_in_u = \
    _cd('helion mass in u')
helion_molar_mass = \
    _cd('helion molar mass')
helion_proton_mass_ratio = \
    _cd('helion-proton mass ratio')
hertz_atomic_mass_unit_relationship = \
    _cd('hertz-atomic mass unit relationship')
hertz_electron_volt_relationship = \
    _cd('hertz-electron volt relationship')
hertz_hartree_relationship = \
    _cd('hertz-hartree relationship')
hertz_inverse_meter_relationship = \
    _cd('hertz-inverse meter relationship')
hertz_joule_relationship = \
    _cd('hertz-joule relationship')
hertz_kelvin_relationship = \
    _cd('hertz-kelvin relationship')
hertz_kilogram_relationship = \
    _cd('hertz-kilogram relationship')
inverse_fine_structure_constant = \
    _cd('inverse fine-structure constant')
inverse_meter_atomic_mass_unit_relationship = \
    _cd('inverse meter-atomic mass unit relationship')
inverse_meter_electron_volt_relationship = \
    _cd('inverse meter-electron volt relationship')
inverse_meter_hartree_relationship = \
    _cd('inverse meter-hartree relationship')
inverse_meter_hertz_relationship = \
    _cd('inverse meter-hertz relationship')
inverse_meter_joule_relationship = \
    _cd('inverse meter-joule relationship')
inverse_meter_kelvin_relationship = \
    _cd('inverse meter-kelvin relationship')
inverse_meter_kilogram_relationship = \
    _cd('inverse meter-kilogram relationship')
inverse_of_conductance_quantum = \
    _cd('inverse of conductance quantum')
Josephson_constant = \
    _cd('Josephson constant')
joule_atomic_mass_unit_relationship = \
    _cd('joule-atomic mass unit relationship')
joule_electron_volt_relationship = \
    _cd('joule-electron volt relationship')
joule_hartree_relationship = \
    _cd('joule-hartree relationship')
joule_hertz_relationship = \
    _cd('joule-hertz relationship')
joule_inverse_meter_relationship = \
    _cd('joule-inverse meter relationship')
joule_kelvin_relationship = \
    _cd('joule-kelvin relationship')
joule_kilogram_relationship = \
    _cd('joule-kilogram relationship')
kelvin_atomic_mass_unit_relationship = \
    _cd('kelvin-atomic mass unit relationship')
kelvin_electron_volt_relationship = \
    _cd('kelvin-electron volt relationship')
kelvin_hartree_relationship = \
    _cd('kelvin-hartree relationship')
kelvin_hertz_relationship = \
    _cd('kelvin-hertz relationship')
kelvin_inverse_meter_relationship = \
    _cd('kelvin-inverse meter relationship')
kelvin_joule_relationship = \
    _cd('kelvin-joule relationship')
kelvin_kilogram_relationship = \
    _cd('kelvin-kilogram relationship')
kilogram_atomic_mass_unit_relationship = \
    _cd('kilogram-atomic mass unit relationship')
kilogram_electron_volt_relationship = \
    _cd('kilogram-electron volt relationship')
kilogram_hartree_relationship = \
    _cd('kilogram-hartree relationship')
kilogram_hertz_relationship = \
    _cd('kilogram-hertz relationship')
kilogram_inverse_meter_relationship = \
    _cd('kilogram-inverse meter relationship')
kilogram_joule_relationship = \
    _cd('kilogram-joule relationship')
kilogram_kelvin_relationship = \
    _cd('kilogram-kelvin relationship')
a = a_Si_100 = lattice_parameter_of_silicon = \
    _cd('lattice parameter of silicon')
n_0 = Loschmidt_constant = \
    _cd('Loschmidt constant (273.15 K, 101.325 kPa)')
mu_0 = magnetic_constant = \
    _cd('magnetic constant')
Phi_0 = magnetic_flux_quantum = \
    _cd('magnetic flux quantum')
R = molar_gas_constant = \
    _cd('molar gas constant')
M_u = molar_mass_constant = \
    _cd('molar mass constant')
molar_mass_of_carbon_12 = \
    _cd('molar mass of carbon-12')
molar_Planck_constant = \
    _cd('molar Planck constant')
molar_Planck_constant_times_c = \
    _cd('molar Planck constant times c')
molar_volume_of_ideal_gas_ST_100kPa = \
    _cd('molar volume of ideal gas (273.15 K, 100 kPa)')
molar_volume_of_ideal_gas_STP = \
    _cd('molar volume of ideal gas (273.15 K, 101.325 kPa)')
molar_volume_of_silicon = \
    _cd('molar volume of silicon')
Mo_x_unit = \
    _cd('Mo x unit')
lambda_C_mu = muon_Compton_wavelength = \
    _cd('muon Compton wavelength')
muon_Compton_wavelength_over_2_pi = \
    _cd('muon Compton wavelength over 2 pi')
muon_electron_mass_ratio = \
    _cd('muon-electron mass ratio')
g_mu = muon_g_factor = \
    _cd('muon g factor')
mu_mu = muon_magnetic_moment = \
    _cd('muon magnetic moment')
a_mu = muon_magnetic_moment_anomaly = \
    _cd('muon magnetic moment anomaly')
muon_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('muon magnetic moment to Bohr magneton ratio')
muon_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('muon magnetic moment to nuclear magneton ratio')
m_mu = muon_mass = \
    _cd('muon mass')
muon_mass_energy_equivalent = \
    _cd('muon mass energy equivalent')
muon_mass_energy_equivalent_in_MeV = \
    _cd('muon mass energy equivalent in MeV')
muon_mass_in_u = \
    _cd('muon mass in u')
muon_molar_mass = \
    _cd('muon molar mass')
muon_neutron_mass_ratio = \
    _cd('muon-neutron mass ratio')
muon_proton_magnetic_moment_ratio = \
    _cd('muon-proton magnetic moment ratio')
muon_proton_mass_ratio = \
    _cd('muon-proton mass ratio')
muon_tau_mass_ratio = \
    _cd('muon-tau mass ratio')
natural_unit_of_action = \
    _cd('natural unit of action')
natural_unit_of_action_in_eV_s = \
    _cd('natural unit of action in eV s')
natural_unit_of_energy = \
    _cd('natural unit of energy')
natural_unit_of_energy_in_MeV = \
    _cd('natural unit of energy in MeV')
natural_unit_of_length = \
    _cd('natural unit of length')
natural_unit_of_mass = \
    _cd('natural unit of mass')
natural_unit_of_momentum = \
    _cd('natural unit of momentum')
natural_unit_of_momentum_in_MeV_per_c = \
    _cd('natural unit of momentum in MeV/c')
natural_unit_of_time = \
    _cd('natural unit of time')
natural_unit_of_velocity = \
    _cd('natural unit of velocity')
lambda_C_n = neutron_Compton_wavelength = \
    _cd('neutron Compton wavelength')
neutron_Compton_wavelength_over_2_pi = \
    _cd('neutron Compton wavelength over 2 pi')
neutron_electron_magnetic_moment_ratio = \
    _cd('neutron-electron magnetic moment ratio')
neutron_electron_mass_ratio = \
    _cd('neutron-electron mass ratio')
g_n = neutron_g_factor = \
    _cd('neutron g factor')
gamma_n = neutron_gyromagnetic_ratio = \
    _cd('neutron gyromagnetic ratio')
neutron_gyromagnetic_ratio_over_2_pi = \
    _cd('neutron gyromagnetic ratio over 2 pi')
mu_n = neutron_magnetic_moment = \
    _cd('neutron magnetic moment')
neutron_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('neutron magnetic moment to Bohr magneton ratio')
neutron_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('neutron magnetic moment to nuclear magneton ratio')
m_n = neutron_mass = \
    _cd('neutron mass')
neutron_mass_energy_equivalent = \
    _cd('neutron mass energy equivalent')
neutron_mass_energy_equivalent_in_MeV = \
    _cd('neutron mass energy equivalent in MeV')
neutron_mass_in_u = \
    _cd('neutron mass in u')
neutron_molar_mass = \
    _cd('neutron molar mass')
neutron_muon_mass_ratio = \
    _cd('neutron-muon mass ratio')
neutron_proton_magnetic_moment_ratio = \
    _cd('neutron-proton magnetic moment ratio')
neutron_proton_mass_ratio = \
    _cd('neutron-proton mass ratio')
neutron_tau_mass_ratio = \
    _cd('neutron-tau mass ratio')
neutron_to_shielded_proton_magnetic_moment_ratio = \
    _cd('neutron to shielded proton magnetic moment ratio')
G = Newtonian_constant_of_gravitation = \
    _cd('Newtonian constant of gravitation')
Newtonian_constant_of_gravitation_over_h_bar_c = \
    _cd('Newtonian constant of gravitation over h-bar c')
mu_N = nuclear_magneton = \
    _cd('nuclear magneton')
nuclear_magneton_in_eV_per_T = \
    _cd('nuclear magneton in eV/T')
nuclear_magneton_in_inverse_meters_per_tesla = \
    _cd('nuclear magneton in inverse meters per tesla')
nuclear_magneton_in_K_per_T = \
    _cd('nuclear magneton in K/T')
nuclear_magneton_in_MHz_per_T = \
    _cd('nuclear magneton in MHz/T')
h = Planck_constant = \
    _cd('Planck constant')
Planck_constant_in_eV_s = \
    _cd('Planck constant in eV s')
Planck_constant_over_2_pi = \
    _cd('Planck constant over 2 pi')
Planck_constant_over_2_pi_in_eV_s = \
    _cd('Planck constant over 2 pi in eV s')
Planck_constant_over_2_pi_times_c_in_MeV_fm = \
    _cd('Planck constant over 2 pi times c in MeV fm')
l_P = Planck_length = \
    _cd('Planck length')
m_P = Planck_mass = \
    _cd('Planck mass')
Planck_mass_energy_equivalent_in_GeV = \
    _cd('Planck mass energy equivalent in GeV')
T_P = Planck_temperature = \
    _cd('Planck temperature')
t_P = Planck_time = \
    _cd('Planck time')
proton_charge_to_mass_quotient = \
    _cd('proton charge to mass quotient')
lambda_C_p = proton_Compton_wavelength = \
    _cd('proton Compton wavelength')
proton_Compton_wavelength_over_2_pi = \
    _cd('proton Compton wavelength over 2 pi')
proton_electron_mass_ratio = \
    _cd('proton-electron mass ratio')
g_p = proton_g_factor = \
    _cd('proton g factor')
gamma_p = proton_gyromagnetic_ratio = \
    _cd('proton gyromagnetic ratio')
proton_gyromagnetic_ratio_over_2_pi = \
    _cd('proton gyromagnetic ratio over 2 pi')
mu_p = proton_magnetic_moment = \
    _cd('proton magnetic moment')
proton_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('proton magnetic moment to Bohr magneton ratio')
proton_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('proton magnetic moment to nuclear magneton ratio')
sigma_prime_p = proton_magnetic_shielding_correction = \
    _cd('proton magnetic shielding correction')
m_p = proton_mass = \
    _cd('proton mass')
proton_mass_energy_equivalent = \
    _cd('proton mass energy equivalent')
proton_mass_energy_equivalent_in_MeV = \
    _cd('proton mass energy equivalent in MeV')
proton_mass_in_u = \
    _cd('proton mass in u')
proton_molar_mass = \
    _cd('proton molar mass')
proton_muon_mass_ratio = \
    _cd('proton-muon mass ratio')
proton_neutron_magnetic_moment_ratio = \
    _cd('proton-neutron magnetic moment ratio')
proton_neutron_mass_ratio = \
    _cd('proton-neutron mass ratio')
R_p = proton_rms_charge_radius = \
    _cd('proton rms charge radius')
proton_tau_mass_ratio = \
    _cd('proton-tau mass ratio')
quantum_of_circulation = \
    _cd('quantum of circulation')
quantum_of_circulation_times_2 = \
    _cd('quantum of circulation times 2')
R_infinity = Rydberg_constant = \
    _cd('Rydberg constant')
Rydberg_constant_times_c_in_Hz = \
    _cd('Rydberg constant times c in Hz')
Rydberg_constant_times_hc_in_eV = \
    _cd('Rydberg constant times hc in eV')
Rydberg_constant_times_hc_in_J = \
    _cd('Rydberg constant times hc in J')
Sackur_Tetrode_constant_ST_100kPa = \
    _cd('Sackur-Tetrode constant (1 K, 100 kPa)')
Sackur_Tetrode_constant_STP = \
    _cd('Sackur-Tetrode constant (1 K, 101.325 kPa)')
c_2 = second_radiation_constant = \
    _cd('second radiation constant')
gamma_prime_h = shielded_helion_gyromagnetic_ratio = \
    _cd('shielded helion gyromagnetic ratio')
shielded_helion_gyromagnetic_ratio_over_2_pi = \
    _cd('shielded helion gyromagnetic ratio over 2 pi')
mu_prime_h = shielded_helion_magnetic_moment = \
    _cd('shielded helion magnetic moment')
shielded_helion_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('shielded helion magnetic moment to Bohr magneton ratio')
shielded_helion_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('shielded helion magnetic moment to nuclear magneton ratio')
shielded_helion_to_proton_magnetic_moment_ratio = \
    _cd('shielded helion to proton magnetic moment ratio')
shielded_helion_to_shielded_proton_magnetic_moment_ratio = \
    _cd('shielded helion to shielded proton magnetic moment ratio')
gamma_prime_p = shielded_proton_gyromagnetic_ratio = \
    _cd('shielded proton gyromagnetic ratio')
shielded_proton_gyromagnetic_ratio_over_2_pi = \
    _cd('shielded proton gyromagnetic ratio over 2 pi')
mu_prime_p = shielded_proton_magnetic_moment = \
    _cd('shielded proton magnetic moment')
shielded_proton_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('shielded proton magnetic moment to Bohr magneton ratio')
shielded_proton_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('shielded proton magnetic moment to nuclear magneton ratio')
c = c_0 = speed_of_light_in_vacuum = \
    _cd('speed of light in vacuum')
g = g_n = standard_acceleration_of_gravity = \
    _cd('standard acceleration of gravity')
atm = standard_atmosphere = \
    _cd('standard atmosphere')
sigma = Stefan_Boltzmann_constant = \
    _cd('Stefan-Boltzmann constant')
lambda_C_tau = tau_Compton_wavelength = \
    _cd('tau Compton wavelength')
tau_Compton_wavelength_over_2_pi = \
    _cd('tau Compton wavelength over 2 pi')
tau_electron_mass_ratio = \
    _cd('tau-electron mass ratio')
m_tau = tau_mass = \
    _cd('tau mass')
tau_mass_energy_equivalent = \
    _cd('tau mass energy equivalent')
tau_mass_energy_equivalent_in_MeV = \
    _cd('tau mass energy equivalent in MeV')
tau_mass_in_u = \
    _cd('tau mass in u')
tau_molar_mass = \
    _cd('tau molar mass')
tau_muon_mass_ratio = \
    _cd('tau-muon mass ratio')
tau_neutron_mass_ratio = \
    _cd('tau-neutron mass ratio')
tau_proton_mass_ratio = \
    _cd('tau-proton mass ratio')
sigma_e = Thomson_cross_section = \
    _cd('Thomson cross section')
triton_electron_magnetic_moment_ratio = \
    _cd('triton-electron magnetic moment ratio')
triton_electron_mass_ratio = \
    _cd('triton-electron mass ratio')
g_t = triton_g_factor = \
    _cd('triton g factor')
mu_t = triton_magnetic_moment = \
    _cd('triton magnetic moment')
triton_magnetic_moment_to_Bohr_magneton_ratio = \
    _cd('triton magnetic moment to Bohr magneton ratio')
triton_magnetic_moment_to_nuclear_magneton_ratio = \
    _cd('triton magnetic moment to nuclear magneton ratio')
m_t = triton_mass = \
    _cd('triton mass')
triton_mass_energy_equivalent = \
    _cd('triton mass energy equivalent')
triton_mass_energy_equivalent_in_MeV = \
    _cd('triton mass energy equivalent in MeV')
triton_mass_in_u = \
    _cd('triton mass in u')
triton_molar_mass = \
    _cd('triton molar mass')
triton_neutron_magnetic_moment_ratio = \
    _cd('triton-neutron magnetic moment ratio')
triton_proton_magnetic_moment_ratio = \
    _cd('triton-proton magnetic moment ratio')
triton_proton_mass_ratio = \
    _cd('triton-proton mass ratio')
u = unified_atomic_mass_unit = \
    _cd('unified atomic mass unit')
R_K = von_Klitzing_constant = \
    _cd('von Klitzing constant')
weak_mixing_angle = \
    _cd('weak mixing angle')
b_prime = Wien_frequency_displacement_law_constant = \
    _cd('Wien frequency displacement law constant')
b = Wien_wavelength_displacement_law_constant = \
    _cd('Wien wavelength displacement law constant')

del absolute_import, _math, _pc, Quantity, _cd
