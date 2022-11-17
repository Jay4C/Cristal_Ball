import math
import unittest
from pylatex import Document, Command
from pylatex.utils import NoEscape
import ahkab
from ahkab import time_functions
from sympy import Function, Derivative, pprint, Eq
# x is the independent variable
from sympy.abc import x
from sympy.solvers.ode import *
import matplotlib.pyplot as plt
import numpy as np


class UnitTestsDSIBSMBUS4936961WithPylatex(unittest.TestCase):
    def test_demonstration_inducteur_a_air_with_pylatex(self):
        doc = Document('inductor')

        # Preamble of the document
        doc.preamble.append(Command('title', 'US patent n°4,936,961 - Demonstration for inductor'))
        doc.preamble.append(Command('author', ''))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.preamble.append(Command('usepackage', NoEscape(r'amsmath')))
        doc.preamble.append(Command('usepackage', NoEscape(r'circuitikz')))
        doc.append(NoEscape(r'\maketitle'))

        doc.append(NoEscape(r'\underline{Course}'))
        doc.append('\n')
        doc.append('A coil is formed from a wire wound either in air or on a magnetic core. '
                   'A driver traveled by a current i(t) creates a magnetic field, of flux ')
        doc.append(NoEscape(r"$\boxed{\Phi}$"))
        doc.append(', such than :')
        doc.append(NoEscape(r"$\boxed{\Phi = L * i(t)}$"))

        doc.append('\n')
        doc.append('\n')

        doc.append("The coefficient L is the inductance of the coil. Lenz-Faraday's law links the flow ")
        doc.append(NoEscape(r"$\boxed{\Phi}$"))
        doc.append(' to the f.é.m. u:')
        doc.append(NoEscape(r"$\boxed{u(t) = L * \frac{\mathrm d \Phi}{\mathrm d t}}$"))

        doc.append('\n')
        doc.append('\n')

        doc.append('The electrical characteristic of a coil is then given by :')
        doc.append(NoEscape(r"$\boxed{u(t) = L * \frac{\mathrm d i}{\mathrm d t}}$"))

        doc.append('\n')
        doc.append('\n')

        doc.append('The inductance L of a coil depends on the geometry, the number of turns N, the magnetic circuit '
                   'Ex. : The inductance of a solenoid in air with 1 layer of N turns, of section')
        doc.append(NoEscape(r'$\boxed{S = \pi * r^{2}}$'))
        doc.append('and of length')
        doc.append(NoEscape(r'$\boxed{l \gg r}$'))
        doc.append(':')
        doc.append(NoEscape(r'$\boxed{L = \mu_{0} * \frac{S * N^{2}}{l}}$'))
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{\mu_{0} = 4 * \pi * 10^{-7} H/m}$'))
        doc.append('is the permeability of the vacuum.')
        doc.append('\n')
        doc.append('L in henry ; S in square meter ; l in meter ; r in meter')

        doc.append('\n')
        doc.append('\n')

        doc.append('One of the useful characteristics of a winding produced with any magnetic core is the value')
        doc.append(NoEscape(r'$\boxed{L = \mu_{0} * \mu_{r} * \frac{S * N^{2} * S_{m}}{l_{m}}}$'))
        doc.append('\n')
        doc.append(NoEscape(r'\boxed{\mu_{r}}'))
        doc.append(': the relative permeability of the magnetic circuit;')
        doc.append('\n')
        doc.append(NoEscape(r'\boxed{S_{m}, l_{m}}'))
        doc.append(': area and average length.')

        doc.append('\n')
        doc.append('\n')

        doc.append('A coil stores energy in electromagnetic form when a current flows through it. '
                   'The energy stored in a coil crossed by a current i at time t : ')
        doc.append(NoEscape(r'$\boxed{E = \frac{1}{2} * L * i^{2}}$'))
        doc.append('\n')
        doc.append('The power supplied to the inductor : ')
        doc.append(NoEscape(r'$\boxed{P = \frac{1}{2} * L * \frac{\mathrm d i^{2}(t)}{\mathrm d t} }$'))
        doc.append('\n')
        doc.append('It is difficult to quickly vary the current flowing in a coil, '
                   'especially since the value of its inductance L will be large.')

        doc.append('\n')
        doc.append('\n')

        doc.append('An ideal coil would have no loss of energy, but in reality, the conductor used for the winding '
                   'also has a certain resistance which causes losses by Joule effect. The fact that the stored '
                   'energy corresponds to a current flow gives the coil an inertia effect for the current. '
                   'In particular, this current cannot be discontinuous. The use of a magnetic core makes it '
                   'possible to reduce the number of turns for a given inductance, therefore the losses by Joule '
                   'effect. However, there are also two types of losses in magnetic cores: 1. Losses by hysteresis '
                   'proportional to the frequency; 2. The eddy current losses proportional to the square of the '
                   'frequency. To account for these losses, a loss resistance R is introduced in series with L, '
                   'or a resistance in parallel ')
        doc.append(NoEscape(r'$\boxed{R_{p}}$'))
        doc.append('.')

        doc.append('\n')
        doc.append('\n')

        doc.append('Due to these physical properties, the coils are components that can hardly be miniaturized, '
                   'and therefore very little used in on-board electronic circuits and even less in integrated '
                   'circuits (ICs). Main characteristics of the inductors: The value of the inductor; '
                   'Resistance of losses; The admissible current; Temperature coefficient, ')
        doc.append(NoEscape(r'$\boxed{\alpha}$'))

        doc.append('\n')
        doc.append('\n')

        doc.append('Different categories: Air coils: Low inductance, Limited magnetic saturation, '
                   'eg. used for high frequencies; Ferrite core coils: High inductance (for inductances '
                   'from 0: 1 microH to 10 mH there are “miniature” coils resembling resistors.), '
                   'Common frequency ranges 1 kHz to 100 kHz (but it is possible to extend to 1 GHz.) '
                   'Close to saturation, the presence of the nucleus introduces non-linearities.')

        doc.append('\n')
        doc.append('\n')
        doc.append('\n')

        doc.append(NoEscape(r'\underline{Calculations}'))
        doc.append('\n')
        doc.append('We have the features : ')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                N = 100 \\
                r = 1,27 * 10^{-2} \\
                S = r^{2} = 1,6129 * 10^{-4} \\
                l = 10 * 10^{-2} \\
                \mu_{0} = 4 * \pi * 10^{-7} \\
                L = 2,03 * 10^{-5}
                \end{cases}
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append('N in turns ; r in meter ; S in meter^(2) ; l in meter ; L in henry ; ')
        doc.append(NoEscape(r'$\mu_{0}$'))
        doc.append('in henry per meter')

        doc.generate_pdf(clean_tex=True)

    def test_demonstration_condensateur_with_pylatex(self):
        doc = Document('capacitor')

        # Preamble of the document
        doc.preamble.append(Command('title', 'US patent n°4,936,961 - Demonstration for capacitor'))
        doc.preamble.append(Command('author', ''))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.preamble.append(Command('usepackage', NoEscape(r'amsmath')))
        doc.preamble.append(Command('usepackage', NoEscape(r'circuitikz')))
        doc.append(NoEscape(r'\maketitle'))

        doc.append(NoEscape(r'\underline{Course}'))

        doc.append('\n')

        doc.append('A capacitor is a passive linear dipole made up of two armatures separated by a dielectric. '
                   'Under the action of a voltage u(t) charges will accumulate opposite one another. '
                   'The capacitor is characterized by the proportionality coefficient between the amount '
                   'of charge stored and the voltage:')
        doc.append(NoEscape(r'$\boxed{ i(t) = C * \frac{\mathrm d u}{\mathrm d t} }$'))

        doc.append('\n')
        doc.append('\n')

        doc.append('The capacitance C depends both on the geometry of the reinforcements and on the nature '
                   'of the dielectric. Ex.: The capacity of a plane capacitor of section S '
                   'whose dielectric has a thickness e:')
        doc.append(NoEscape(r'$\boxed{C = \epsilon * \frac{S}{e}}$'))

        doc.append('\n')
        doc.append('\n')

        doc.append(NoEscape(r'$\epsilon = \epsilon_{0} * \epsilon_{r}$'))
        doc.append('is the permittivity of the dielectric.')

        doc.append('\n')
        doc.append('\n')

        doc.append('Energy stored: From an energy point of view, the behavior of the capacitor is very different '
                   'from that of the resistance. As the latter dissipates electrical energy by transforming it '
                   'into heat, the capacitor stores electrical energy when it charges and releases it when it '
                   'discharges. There is very little loss of electrical energy. The charged capacitor therefore '
                   'forms an energy reserve. This energy is expressed as a function of its capacity C and of the '
                   'quantity of charge stored Q according to:')
        doc.append(NoEscape(r'$\boxed{ E = \frac{1}{2} * u * Q = \frac{1}{2} * C * u^{2} }$'))

        doc.append('\n')
        doc.append('\n')

        doc.append('Electric power')
        doc.append(NoEscape(r'$\boxed{ P \equiv \frac{\mathrm d E}{\mathrm d t} }$'))
        doc.append('received by the capacitor is then:')
        doc.append(NoEscape(r'$\boxed{ P = u * C * \frac{\mathrm d u}{\mathrm d t} = u(t) * i(t) }$'))

        doc.append('\n')
        doc.append('\n')

        doc.append('Actual behavior: A capacitor never exhibits pure capacity. In particular, there are always losses '
                   'in the dielectric. These losses are modeled as a first approximation by a resistor R placed '
                   'either in series or in parallel with the capacitance C.')

        doc.append('\n')
        doc.append('\n')

        doc.append('The capacitor is a cylindrical capacitor : ')
        doc.append(NoEscape(r'$\boxed{ C=\frac{2*\pi*\epsilon_{water}*h}{\log_e{\frac{R_{2}}{R_{1}}}} }$'))

        doc.append('\n')
        doc.append('\n')

        doc.append(NoEscape(r'\underline{Calculations}'))
        doc.append('\n')
        doc.append('We have :')
        doc.append('\n')
        doc.append(NoEscape(r'$ \boxed{ |Z_{C}| = \frac{1}{C.\omega} }$'))
        doc.append('\n')
        doc.append(NoEscape(r'$ \boxed{ |\underline{U_{C}}| = |Z_{C}|.|\underline{I_{C}}| }$'))
        doc.append('\n')
        doc.append(NoEscape(r'$ \boxed{ \omega = 2.\pi.f }$'))
        doc.append('\n')
        doc.append('\n')
        doc.append('We have the features :')
        doc.append('\n')
        doc.append(NoEscape(r'''
                $$
                \boxed{
                \begin{cases}
                R_{1} = 6,35 * 10^{-3} \\ 
                R_{2} = 9,525 * 10^{-3} \\
                h = 0,1016 \\ 
                \epsilon_{r} = 80,2 \\
                \epsilon_{water} = 7 * 10^{-10} \\
                \epsilon_{vacuum} = 8,8541878128 * 10^{-12} \\
                C = 1,10209271 * 10^{-9} \\
                f = 10^{4} \\
                \omega = 62831,85 \\
                |Z_{C}| = 14441,16 \\
                |\underline{i_{C}}| = 0,167 \\
                |\underline{U_{C}}| = 2411,67
                \end{cases}
                }
                $$
                '''))

        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{h}$'))
        doc.append('is the length of the cylinders in meter ; ')
        doc.append(NoEscape(r'$\boxed{R_{1}}$'))
        doc.append('is the outside radius of the inner cylinder in meter ; ')
        doc.append(NoEscape(r'$\boxed{R_{2}}$'))
        doc.append('is the outside radius of the outside cylinder in meter ; ')
        doc.append(NoEscape(r'$\boxed{\epsilon_{vacuum}}$'))
        doc.append('is the vacuum permittivity in farad per meter ; ')
        doc.append(NoEscape(r'$\boxed{\epsilon_{r}}$'))
        doc.append('is the relative permittivity of the water without unit ; ')
        doc.append(NoEscape(r'$\boxed{\epsilon_{water}}$'))
        doc.append('is the water permittivity ; ')
        doc.append(NoEscape(r'$\boxed{C}$'))
        doc.append('is the capacitance of the capacitor included in the water bath in farad ; ')
        doc.append(NoEscape(r'$\boxed{\omega}$'))
        doc.append('is the frequency in radian per second ; ')
        doc.append(NoEscape(r'$\boxed{Z_{C}}$'))
        doc.append('is the impedance of the capacitor in ohms ; ')
        doc.append(NoEscape(r'$\boxed{I_{C}}$'))
        doc.append('is the current into the capacitor in amperes ; ')
        doc.append(NoEscape(r'$\boxed{U_{C}}$'))
        doc.append('is the voltage of the capacitor in volts ; ')
        doc.append(NoEscape(r'$\boxed{f}$'))
        doc.append('is the frequency of the circuit in Hz')

        doc.generate_pdf(clean_tex=True)

    def test_demonstration_transformateur_with_pylatex(self):
        doc = Document('transformer')

        # Preamble of the document
        doc.preamble.append(Command('title', 'US patent n°4,936,961 - Demonstration for transformer'))
        doc.preamble.append(Command('author', ''))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.preamble.append(Command('usepackage', NoEscape(r'amsmath')))
        doc.preamble.append(Command('usepackage', NoEscape(r'circuitikz')))
        doc.append(NoEscape(r'\maketitle'))

        doc.append(NoEscape(r'\underline{Course}'))

        doc.append('\n')

        doc.append('The transformer transfers energy (in alternative form) from a source to a load, '
                   'while modifying the value of the voltage. The tension can either be raised or lowered '
                   'depending on the intended use. The change from one voltage level to another is '
                   'done by the effect of a magnetic field.')

        doc.append('\n')
        doc.append('\n')

        doc.append('Among the transformer applications, we note: 1. Electronics: (a) low voltage power '
                   'supply; (b) impedance matching 2. Electrical engineering: (a) transformation of the voltage '
                   'for the transport and distribution of electricity (b) low-voltage power supply '
                   '(for example, halogen lamps) 3. Measurement: (a) transformers d current intensity '
                   '(b) potential transformers. There are two main types of transformers, the battleship '
                   'type and the column type. In the battleship type, a magnetic circuit with three branches '
                   'is used, and the windings are around the central branch. In the column type, a two-column '
                   'magnetic circuit is used.')

        doc.append('\n')
        doc.append('\n')

        doc.append('The transformer consists of two (or more) windings coupled on a magnetic core.')

        doc.append('\n')
        doc.append('\n')

        doc.append('The side of the source is called the primary. The side of the load is called the secondary. '
                   'The flow (phi) is the mutual flow.')

        doc.append('\n')
        doc.append('\n')

        doc.append("It should be noted that there is no electrical connection between the primary and the secondary. "
                   "The entire coupling between the two windings is magnetic. When an AC voltage is applied to the "
                   "source, this creates an AC flux in the magnetic core. According to Faraday's law, "
                   "this flux creates electromotive forces in the coils. The induced electromotive force "
                   "is proportional to the number of turns in the coil and to the rate of change of flux. "
                   "According to the ratio of the number of turns between the primary and the secondary, "
                   "the secondary supplies the load with a voltage different from that of the source.")

        doc.append('\n')
        doc.append('\n')

        doc.append(NoEscape(r'\underline{Ideal transformer}'))

        doc.append('\n')
        doc.append('\n')

        doc.append('We define an ideal transformer with the following characteristics: '
                   '1 - The resistance in the wires (primary and secondary) is zero. '
                   '2 - The magnetic core is perfect (mu_r = infinity, ro = 0). '
                   'If we study the implications of these simplifications, we see that the reluctance of '
                   'the core will be zero, and therefore there is no leakage. The flow is therefore '
                   'completely contained inside the core. The magnetic coupling between primary and '
                   'secondary is perfect; all the flow from primary goes to secondary. [A coupling parameter, '
                   'k, is defined in the non-ideal case; for an ideal transformer, k = 1.]')

        doc.append('\n')
        doc.append('\n')

        doc.append('We have : ')
        doc.append(NoEscape(r'$\boxed{N_{1} * I_{1} - N_{2} * I_{2} =  \Re * \phi = 0 }$'))

        doc.append('\n')

        doc.append(NoEscape(r'$\boxed{N_{1}}$'))
        doc.append('is the number of turns of the primary coil of the transformer ; ')
        doc.append(NoEscape(r'$\boxed{N_{2}}$'))
        doc.append('is the number of turns of the secondary coil of the transformer ; ')
        doc.append(NoEscape(r'$\boxed{\Re}$'))
        doc.append('is the reluctance of the core ; ')
        doc.append(NoEscape(r'$\boxed{\phi}$'))
        doc.append('is the magnetic flow in the core')

        doc.append('\n')
        doc.append('\n')

        doc.append('The transformation ratio (a without unit) is defined as the ratio of the number of turns of the '
                   'transformer. So : ')
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{a = \frac{N_{1}}{N_{2}} = \frac{V_{1}}{V_{2}}}$'))
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{V_{1}}$'))
        doc.append('is the voltage across the primary coil of the transformer in volt; ')
        doc.append(NoEscape(r'$\boxed{V_{2}}$'))
        doc.append('is the voltage across the secondary coil of the transformer in volt')

        doc.append('\n')
        doc.append('\n')

        doc.append('Hence we find : ')
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{\frac{I_{1}}{I_{2}} = \frac{N_{2}}{N_{1}} = \frac{1}{a}}$'))
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{I_{1}}$'))
        doc.append('is the current into the primary coil of the transformer in ampere; ')
        doc.append(NoEscape(r'$\boxed{I_{2}}$'))
        doc.append('is the current into the secondary coil of the transformer in ampere; ')

        doc.append('\n')
        doc.append('\n')

        doc.append(NoEscape(r'\underline{Toroidal transformers}'))

        doc.append('\n')

        doc.append("Toroidal transformers are inductors and transformers which use magnetic cores "
                   "with a toroidal (ring or donut) shape. They are passive electronic components, consisting "
                   "of a circular ring or donut shaped magnetic core of ferromagnetic material such as laminated "
                   "iron, iron powder, or ferrite, around which wire is wound. though in the past, closed-core "
                   "inductors and transformers often used cores with a square shape, the use of toroidal-shaped "
                   "cores has increased greatly because of their superior electrical performance. The advantage "
                   "of the toroidal shape is that, due to its symmetry, the amount of magnetic flux that escapes "
                   "outside the core (leakage flux) is low, therefore it is more efficient and thus radiates less "
                   "electromagnetic interference (EMI). Toroidal inductors and transformers are used in a wide range "
                   "of electronic circuits: power supplies, inverters, and amplifiers, which in turn are used in the "
                   "vast majority of electrical equipment: TVs, radios, computers, and audio systems.")

        doc.append('\n')

        doc.append("In general, a toroidal inductor/transformer is more compact than other shaped cores because "
                   "they are made of fewer materials and include a centering washer, nuts, and bolts resulting in "
                   "up to a 50% lighter weight design. This is especially the case for power devices. Because "
                   "the toroid is a closed-loop core it will have a higher magnetic field and thus higher "
                   "inductance and Q factor than an inductor of the same mass with a straight core (solenoid coils). "
                   "This is because most of the magnetic field is contained within the core. By comparison, with an "
                   "inductor with a straight core, the magnetic field emerging from one end of the core has a long "
                   "path through air to enter the other end. In addition, because the windings are relatively short "
                   "and wound in a closed magnetic field, a toroidal transformer will have a lower secondary "
                   "impedance which will increase efficiency, electrical performance and reduce effects such as "
                   "distortion and fringing. Due to the symmetry of a toroid, little magnetic flux escapes from the "
                   "core (leakage flux). Thus a toroidal inductor/transformer, radiates less electromagnetic "
                   "interference (EMI) to adjacent circuits and is an ideal choice for highly concentrated "
                   "environments. Manufacturers have adopted toroidal coils in recent years to comply with "
                   "increasingly strict international standards limiting the amount of electromagnetic field "
                   "consumer electronics can produce.")

        doc.append('\n')
        doc.append('\n')

        doc.append(NoEscape(r'\underline{Calculations}'))

        doc.append('\n')
        doc.append('\n')

        doc.append('We have the features :')
        doc.append('\n')
        doc.append(NoEscape(r'''
                        $$
                        \boxed{
                        \begin{cases}
                        N_{1} = 200 \\
                        N_{2} = 600 \\
                        A = 9.10^{-6} \\
                        l_{1} = 1.10^{-2} \\
                        l_{2} = 1.10^{-2} \\
                        \mu_{r} = 1,26.10^{-4} \\
                        L_{1} = 0,004536 \\
                        L_{2} = 0,040824 \\
                        a = \frac{1}{3} \\
                        V_{1} = 26 \\
                        V_{2} = 78 \\
                        I_{1} = 0,5 \\
                        I_{2} = 0,167 \\
                        D_{o} = 39 \\
                        T_{c} = 3 \\
                        T_{D_{o} - D_{i}} = 7
                        \end{cases}
                        }
                        $$
                        '''))
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{\mu_{r}}$'))
        doc.append('is the relative permeability of the magnetic circuit in henry per meter ; ')
        doc.append(NoEscape(r'$\boxed{D_{o}}$'))
        doc.append('is the outside diameter of the toroid core in millimeter ; ')
        doc.append(NoEscape(r'$\boxed{T_{c}}$'))
        doc.append('is the thickness of the toroid core in millimeter ; ')
        doc.append(NoEscape(r'$\boxed{T_{D_{o} - D_{i}}}$'))
        doc.append('is the space between the outside diameter and inside diameter in millimeter ; ')
        doc.append(NoEscape(r'$\boxed{A}$'))
        doc.append('is the area of the toroid core in square meter')
        doc.append(NoEscape(r'$\boxed{L_{1}}$'))
        doc.append('is the inductance of the primary winding of the transformer in henry ; ')
        doc.append(NoEscape(r'$\boxed{L_{2}}$'))
        doc.append('is the inductance of the secondary winding of the transformer in henry ; ')
        doc.append(NoEscape(r'$\boxed{l_{1}}$'))
        doc.append('is the length of the primary winding of the transformer in meter ; ')
        doc.append(NoEscape(r'$\boxed{l_{2}}$'))
        doc.append('is the length of the secondary winding of the transformer in meter')

        doc.generate_pdf(clean_tex=True)

    def test_demonstration_from_paperwork_with_pylatex(self):
        # Full data works
        doc = Document('paperwork')

        # Preamble of the document
        doc.preamble.append(Command('title', 'US patent n°4,936,961 - Demonstration from paperwork'))
        doc.preamble.append(Command('author', ''))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.preamble.append(Command('usepackage', NoEscape(r'amsmath')))
        doc.preamble.append(Command('usepackage', NoEscape(r'circuitikz')))
        doc.preamble.append(Command('usepackage', NoEscape(r'chemfig')))
        doc.preamble.append(Command('usepackage', NoEscape(r'mhchem')))
        doc.append(NoEscape(r'\maketitle'))

        # Equation 1
        doc.append('Equation 1 : ')
        doc.append(NoEscape(r'$\boxed{Z_{series} = (X_{C} - X_{L})}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 2
        doc.append('Equation 2 : ')
        doc.append(NoEscape(r'$\boxed{X_{c} = \frac{1}{2*\pi*f_{C}}}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 3
        doc.append('Equation 3 : ')
        doc.append(NoEscape(r'$\boxed{X_{L} = 2*\pi*f_{L}}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 4
        doc.append('Equation 4 : ')
        doc.append(NoEscape(r'$\boxed{F = \frac{1}{2*\pi*\sqrt{L*C}}}$'))
        doc.append('where F is the resonance frequency of the LC circuit.')

        doc.append('\n')
        doc.append('\n')

        # Equation 5
        doc.append("Equation 5 : Ohm's law for the LC circuit in series is given by ")
        doc.append(NoEscape(r'$\boxed{V_{t} = I * Z_{series}}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 6
        doc.append('Equation 6 : The voltage ')
        doc.append(NoEscape(r'$\boxed{(V_{L})}$'))
        doc.append('across the inductor (L) is given by the equation : ')
        doc.append(NoEscape(r'$\boxed{V_{L} = V_{t} * \frac{X_{L}}{(X_{L} - X_{C})}}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 7
        doc.append('Equation 7 : The voltage ')
        doc.append(NoEscape(r'$\boxed{(V_{C})}$'))
        doc.append(' across the capacitor (C) is given by the equation : ')
        doc.append(NoEscape(r'$\boxed{V_{C} = V_{t} * \frac{X_{C}}{(X_{L} - X_{C})}}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 8
        doc.append('Equation 8 : ')
        doc.append(NoEscape(r'$\boxed{Z = \sqrt{R_{L}^{2} + (X_{L} - X_{C})^{2}}}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 9
        doc.append('Equation 9 : ')
        doc.append(NoEscape(r'$\boxed{Z = \sqrt{ R_{L} + Z_{2} + Z_{3} + R_{E}}}$'))
        doc.append(' where ')
        doc.append(NoEscape(r'$\boxed{R_{E}}$'))
        doc.append(' is the dielectric constant of natural water.')

        doc.append('\n')
        doc.append('\n')

        # Equation 10
        doc.append("Equation 10 : Ohm's law as to applied electrical power which is ")
        doc.append(NoEscape(r'$\boxed{E = I * R}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 11
        doc.append("Equation 11 : ")
        doc.append(NoEscape(r'$\boxed{P = E * I}$'))

        doc.append('\n')
        doc.append('\n')

        # Equation 12
        doc.append("Equation 12 : ")
        doc.append(NoEscape(r'$\boxed{A = \frac{F}{M}}$'))
        doc.append(' ')
        doc.append("is Newton's law where the acceleration (A) of a particle mass (M) acted on by a net force (F) ")
        doc.append("whereby net force (F) is the force from the Coulomb's law")

        doc.append('\n')
        doc.append('\n')

        # Equation 13
        doc.append("Equation 13 : the Coulomb's law is ")
        doc.append(NoEscape(r"$\boxed{F = \frac{q * q'}{R^{2}}}$"))

        doc.append('\n')
        doc.append('\n')

        # Equation 14
        doc.append("Equation 14 : ")
        doc.append(NoEscape(r"$\boxed{V = \frac{q}{e^{R}} or V = \frac{q}{e * R}}$"))

        doc.append('\n')
        doc.append('\n')

        # Equation 15
        doc.append("Equation 15 : ")
        doc.append(NoEscape(r"$\boxed{R_{S} = (V_{in} - V_{led}) / I_{led}}$"))

        doc.append('\n')
        doc.append('\n')

        # Equation 16
        doc.append("Equation 16 : ")
        doc.append(NoEscape(r"$\boxed{P_{W} = V_{cc} * I_{t}}$"))
        doc.append('(LED circuit in parallel array)')

        doc.append('\n')
        doc.append('\n')

        # Equation 17
        doc.append("Equation 17 : ")
        doc.append(NoEscape(r"$\boxed{L_{e} = \sqrt{\frac{Ion^{2} * T_{1}}{(T_{1} + T_{2})}}}$"))

        doc.append('\n')
        doc.append('\n')

        # Voltage intensifier circuit (AA) : figure 1-1
        doc.append("Voltage intensifier circuit (AA) : figure 1-1")
        doc.append('\n')

        doc.append('\n')
        doc.append('\n')

        # Questions
        doc.append("Questions")
        doc.append('\n')
        doc.append(NoEscape(r"$\boxed{R_{2} = ?}$"))
        doc.append('\n')
        doc.append(NoEscape(r"$\boxed{R_{3} = ?}$"))
        doc.append('\n')
        doc.append("Number of turns of (G) = ?")
        doc.append('\n')
        doc.append("Number of turns of (A) = ?")
        doc.append('\n')
        doc.append(NoEscape(r"$\boxed{R_{1} = ?}$"))
        doc.append('\n')
        doc.append("Number of turns of (C) = ?")
        doc.append('\n')
        doc.append("Number of turns of (D) = ?")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-2 : LC circuit
        doc.append("Figure 1-2 : LC circuit")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-3 : applied voltage to plates
        doc.append("Figure 1-3 : applied voltage to plates")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-4 : applied voltage to resonant cavity
        doc.append("Figure 1-4 : applied voltage to resonant cavity")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-5 : Variable amplitude gated unipolar pulse frequency dynamically
        # controls hydrogen gas yield on demand while inhibiting amp flow
        doc.append("Figure 1-5 : Variable amplitude gated unipolar pulse frequency dynamically "
                   "controls hydrogen gas yield on demand while inhibiting amp flow")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-6 : Voltage potential performing work
        doc.append("Figure 1-6 : Voltage potential performing work")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-7 : Electrical charges of the water molecule
        doc.append("Figure 1-7 : Electrical charges of the water molecule")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-8 : Hydrogen fracturing process
        doc.append("Figure 1-8 : Hydrogen fracturing process")

        doc.append('\n')
        doc.append('\n')

        # Figure 1-9 : Electrical polarization process
        doc.append("Figure 1-9 : Electrical polarization process")

        doc.append('\n')
        doc.append('\n')

        # Voltage intensifier circuit (AA) : Figure 1-1
        doc.append("Voltage intensifier circuit (AA) : Figure 1-1")
        doc.append('\n')
        doc.append("Démonstration : ")

        doc.append('\n')
        doc.append(NoEscape(r"$\boxed{U_{C1} = 1 000 V}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{U_{L1} = 10 V}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{f_{1} = 10 kHz}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{i_{1} = 500 mA}$"))

        doc.append("\n")
        doc.append("Onde sinusoïdale et duty cycle = 50%. ")

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{C = \frac{Q}{U}}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{L = \frac{N^{2} * \mu * A}{l}}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{U_{L}(t) = + L * \frac{\mathrm d}{\mathrm d t} \left( i_{L}(t) \right)}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{i_{C}(t) = C * \frac{\mathrm d}{\mathrm d t} \left( U_{C}(t) \right)}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{U_{L}(t) = R_{L} * i_{L}(t) "
                            r"+ L * \frac{\mathrm d}{\mathrm d t} \left( i_{L}(t) \right)}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{m = \frac{\underline{U_{2}}}{\underline{U_{1}}} "
                            r"= \frac{N_{2}}{N_{1}} = \frac{I_{1}}{I_{2}}}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{f = \frac{1}{T}}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{\omega = 2 * \pi * f}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{D = \frac{PW}{T}}$"))
        doc.append("where D : duty cycle ; PW : pulse width ; T : total period of the signal")

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{\underline{Z_{L}} = R_{L} + j * L * \omega}$"))

        doc.append("\n")
        doc.append(NoEscape(r"$\boxed{\underline{Z_{C}} = \frac{1}{j * C * \omega}}$"))

        doc.append("\n")
        doc.append("Schéma impédance :")

        doc.append("\n")
        doc.append("\n")

        doc.append("D'après la loi des mailles, on a : ")
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (1) : \underline{U_{L_{1 bis}}}
                &= \underline{Z_{2}} * \underline{i_{2}} + \underline{U_{C_{1}}} + \underline{Z_{3}} * \underline{i_{2}} 
                \\ &= (R_{L_{2}} + j * L_{2} * \omega) * \underline{i_{2}} + \frac{1}{j * C_{1} * \omega} 
                * \underline{i_{2}} + (R_{L_{3}} + j * L_{3} * \omega) * \underline{i_{2}} 
                \\ &= \underline{i_{2}} * (R_{L_{2}} + j * L_{2} * \omega + \frac{1}{j * C_{1} * \omega} + R_{L_{3}} 
                + j * L_{3} * \omega)
                \\ &= \underline{i_{2}} * \frac{1 + j * C_{1} * \omega * (R_{L_{2}} + j * L_{2} * \omega + R_{L_{3}} 
                + j * L_{3} * \omega)}{j * C_{1} * \omega}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append("\n")

        doc.append(
            NoEscape(
                r'''
                $
                \boxed{
                (2) : \underline{U_{C_{1}}} = \underline{Z_{C_{1}}} * \underline{i_{2}}
                }
                $
                '''
            )
        )

        doc.append("\n")

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (2) \iff \mid \underline{i_{2}} \mid 
                &= \frac{\mid \underline{U_{C_{1}}} \mid}{\mid \underline{Z_{C_{1}}} \mid} \\
                &= \frac{\mid \underline{U_{C_{1}}} \mid}{\frac{\mid 1 \mid}{\mid j * C_{1} * \omega \mid}} \\
                &= \mid \underline{U_{C_{1}}} \mid * \mid j * C_{1} * \omega \mid \\
                &= 1000 * \sqrt{(C_{1} * \omega)^{2}} \\
                &= 1000 * C_{1} * \omega
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (1) \iff \underline{U_{L_{1 bis}}} 
                &= \underline{i_{2}} . \frac{ ( 1 + j . R_{L_{2}} . C_{1} . \omega - L_{2} . C_{1} . \omega^{2} 
                + j . R_{L_{3}} . C_{1} . \omega - L_{3} . C_{1} . \omega^{2} ) }{ ( j . C_{1} . \omega ) } \\
                &= \underline{i_{2}} . \frac{ [ ( 1 - L_{2} . C_{1} . \omega^{2} - L_{3} . C_{1} . \omega^{2} ) 
                + j . ( R_{L_{2}} . C_{1} . \omega + R_{L_{3}} . C_{1} . \omega ) ] }{ ( j . C_{1} . \omega ) }
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (3) : \mid \underline{U_{L_{1 bis}}} \mid
                &= \mid \underline{i_{2}} \mid . \frac{ \mid [ ( 1 - L_{2} . C_{1} . \omega^{2} - L_{3} . 
                C_{1} . \omega^{2} ) + j . ( R_{L_{2}} . C_{1} . \omega + R_{L_{3}} . C_{1} . \omega ) ] \mid }
                { \mid ( j . C_{1} . \omega ) \mid} \\
                &= 1000 . C_{1} . \omega . \frac{ \sqrt{ ( 1 - L_{2} . C_{1} . \omega^{2} - L_{3} . C_{1} . 
                \omega^{2} )^{2} + ( R_{L_{2}} . C_{1} . \omega + R_{L_{3}} . C_{1} . \omega )^{2} } }
                { ( C_{1} . \omega ) } \\
                &= 1000 . \sqrt{ ( 1 - L_{2} . C_{1} . \omega^{2} - L_{3} . C_{1} . 
                \omega^{2} )^{2} + ( R_{L_{2}} . C_{1} . \omega + R_{L_{3}} . C_{1} . \omega )^{2} } \\
                &= 1000 . \sqrt{ ( 1 - C_{1} . \omega^{2} . ( L_{2} + L_{3}) )^{2} + ( C_{1} . \omega 
                . ( R_{L_{2}} + R_{L_{3}} ) )^{2} }
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Or,')
        doc.append(NoEscape(r'$\boxed{\mid \underline{U_{L_{1 bis}}} \mid = 78}$'))

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (3) &\iff 1000 . \sqrt{ ( 1 - C_{1} . \omega^{2} . ( L_{2} + L_{3}) )^{2} + ( C_{1} . \omega 
                . ( R_{L_{2}} + R_{L_{3}} ) )^{2} } = 78 \\
                &\iff \sqrt{ ( 1 - C_{1} . \omega^{2} . ( L_{2} + L_{3}) )^{2} + ( C_{1} . \omega 
                . ( R_{L_{2}} + R_{L_{3}} ) )^{2} } = \frac{78}{1000} \\
                &\iff ( 1 - C_{1} . \omega^{2} . ( L_{2} + L_{3}) )^{2} + ( C_{1} . \omega 
                . ( R_{L_{2}} + R_{L_{3}} ) )^{2} = (\frac{78}{1000})^{2} \\
                &\iff ( 1 - C_{1} . (2 . \pi . 10^{4})^{2} . ( L_{2} + L_{3}) )^{2} + ( C_{1} . 2 . \pi . 10^{4} 
                . ( R_{L_{2}} + R_{L_{3}} ) )^{2} = (\frac{78}{1000})^{2}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Or,')
        doc.append(
            NoEscape(
                r'''
                $
                \boxed{ 
                \frac{ \mid \underline{U_{L_{1 bis}}} \mid }{\mid \underline{U_{L_{1}}} \mid } 
                = \frac{ 78 }{ 26 } 
                = 3
                }
                $
                '''
            )
        )

        doc.append('\n')

        doc.append('Or,')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                \frac{ \mid \underline{I_{1}} \mid }{ \mid \underline{I_{2}} \mid } = 3 
                \iff \frac{ 500 . 10^{-3} }{ \mid \underline{I_{2}} \mid } = 3 \\
                \iff \mid \underline{I_{2}} \mid = \frac{ 500 . 10^{-3} }{ 3 } = 166,67 . 10^{-3} \\
                \iff \mid \underline{I_{2}} \mid = 1000 . C_{1} . \omega \\
                \iff C_{1} = \frac{ \mid \underline{I_{2}} \mid }{ 1000 . 2 . \pi . 10^{4} } \\
                \iff C_{1} = \frac{ 166,67 . 10^{-3} }{ 10^{7} . 2 . \pi } \\
                \iff C_{1} = 2,7 * 10^{-9}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Or,')
        doc.append(
            NoEscape(
                r'''
                $
                \boxed{ 
                N_{L_{1}} = 200
                }
                $
                '''
            )
        )
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $
                \boxed{ 
                N_{L_{1 bis}} = 600
                }
                $
                '''
            )
        )

        doc.append('\n')

        doc.append("Or, ")
        doc.append(
            NoEscape(
                r'''
                $
                \boxed{ 
                (3) \iff ( 1 - 4 . 10^{-11} . (2 . \pi . 10^{4})^{2} . (L_{2} + L_{3})^{2} )^{2} 
                + ( 4 . 10^{-11} . 2 . \pi . 10^{4} . ( R_{L_{2}} + R_{L_{3}} )^{2} = 0,006084        
                }
                $
                '''
            )
        )

        doc.append('\n')

        doc.append("D'après la loi des mailles dans la maille (a) en impédance complexe, on a :")
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (4) 
                \iff \underline{U_{L_{1 bis}}} = \underline{U_{C_{1}}} + \underline{U_{L_{2}, R_{2}}} 
                + \underline{U_{L_{3}, R_{3}}} \\
                \iff \underline{U_{L_{1 bis}}} - \underline{U_{C_{1}}} = \underline{U_{L_{2}, R_{2}}} 
                + \underline{U_{L_{3}, R_{3}}} \\
                \iff \mid \underline{U_{L_{1 bis}}} - \underline{U_{C_{1}}} \mid = \mid \underline{U_{L_{2}, R_{2}}} 
                + \underline{U_{L_{3}, R_{3}}} \mid \\
                \iff \mid \underline{U_{L_{1 bis}}} - \underline{U_{C_{1}}} \mid \leq 
                \mid \underline{U_{L_{1 bis}}} \mid - \mid \underline{U_{C_{1}}} \mid
                \end{aligned} \\
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('\n')
        doc.append('\n')

        doc.append('Demonstrate that the rise in voltage, the rise in frequency, the lowering of the current '
                   'greatly influence the functioning of water electrolysis.')

        doc.append('\n')
        doc.append('\n')

        doc.append('Chemical formula for water electrolysis : ')
        doc.append('\n')
        doc.append('Cathode : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \schemestart \ce{2H+} + \ce{2e-} \arrow{->} \ce{H2_{(g)}} \schemestop
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append('Anode : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \schemestart \ce{2H2O_{(l)}} \arrow{->} \ce{O2_{(g)}} + \ce{4H+_{(aq)}} + \ce{4e-} \schemestop
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append('Final reaction : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \schemestart \ce{2H2O_{(l)}} \arrow{->} \ce{O2_{(g)}} + \ce{H2_{(g)}} \schemestop
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('We have :')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                i_{C_{1}} = 166,67 \\
                f = 10
                \end{aligned} \\
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{i_{C_{1}}}$'))
        doc.append('is in mA and f in kHz')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{V_{water}}$'))
        doc.append('be the volume of water used for the electrolysis reaction in ')
        doc.append(NoEscape(r'$m^{3}$'))
        doc.append('.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{\rho_{water}}$'))
        doc.append('be the density of water in ')
        doc.append(NoEscape(r'$\frac{kg}{m^{3}}$'))
        doc.append('.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{n_{water}}$'))
        doc.append('be the amount of water matter or the molar mass of water in ')
        doc.append('mol.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{C_{water}}$'))
        doc.append('be the water concentration in ')
        doc.append(NoEscape(r'$\frac{mol}{m^{3}}$'))
        doc.append('.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{q_{water}}$'))
        doc.append('be the amount of electrons from the electrolysis of water in coulombs.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{f_{water}}$'))
        doc.append('be the resonant frequency of water in Hz.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{E_{v_{water}}}$'))
        doc.append('be the magnitude of vibration or excitation of water in joules.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{V_{\ce{H2_{(g)}}}}$'))
        doc.append('be the volume of dihydrogen produced during the reaction of the electrolysis of '
                   'water in cubic meter.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{V_{\ce{O2_{(g)}}}}$'))
        doc.append('be the volume of dioxygen produced during the reaction of the electrolysis of '
                   'water in cubic meter.')

        doc.append('\n')

        doc.append('It is considered that the radiolysis of water comes into play during the supply of intense '
                   'radiant energy with the use of LEDs. We speak of a break in the water molecule by electronic '
                   'excitation during the ionization phenomenon.')

        doc.append('\n')
        doc.append('We have : ')
        doc.append(NoEscape(r'$\boxed{ V_{\ce{H2_{(g)}}} = 2 . V_{\ce{O2_{(g)}}} }$'))

        doc.append('\n')
        doc.append('How does electronic electron excitation work? By photons. How to excite an electron? It '
                   'is necessary to bring photons to excite the electron thanks to lasers or leds, for example. '
                   'How the excitation levels, vibration levels and rotation levels of the water molecule are '
                   'influenced with the following parameters: 1) increase in the frequency of the electronic '
                   'current greater than or equal to 10 kHz. 2) increase in the voltage across the electrolyser '
                   'greater than or equal to 1000 V. 3) Energy supply in photonic form using LEDs or lasers. '
                   '4) Decrease in the intensity of the electric current less than or equal to 166.67 mA.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{E_{vib_{water}}}$'))
        doc.append('be the vibrational energy of water in joules.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{E_{exc{water}}}$'))
        doc.append('be the energy brought by a photon to the water molecule in joules.')

        doc.append('\n')

        doc.append('Diagram of energy levels of the water molecule')

        doc.append('\n')

        doc.append('What is the resonance frequency of the water molecule? The phenomenon of resonance is nothing '
                   'other than this effect of accumulation of energy by injecting it at the moment when it can be '
                   'added to the energy already accumulated, that is to say, in phase with the latter.')

        doc.append('\n')

        doc.append(NoEscape(r'$\boxed{ E_{da{f}} + E_{i{f}} = E_{r{f}} }$'))
        doc.append('où f est the resonant frequency.')

        doc.append('\n')

        doc.append('The excitation levels, the vibration levels and the rotation levels of the water molecule '
                   'are influenced by: * the increase in the frequency of the alternating electric current greater '
                   'than or equal to 10 kHz because this increases the resonance phenomenon which accumulates a lot '
                   'of energy in the electrolyser cell which will contribute to the ionization energy. '
                   '* the increase in the voltage across the electrolyser cell greater than or equal to 1000 V '
                   'because the cell behaves like a cylindrical capacitor and the charge supplied to the cell '
                   'is proportional to the electric voltage supplied to the cell electrolyser and its capacity. '
                   'So, the higher the voltage, the greater the charge supplied and there will be many more '
                   'electrons at play. * Leds and lasers bring energy to the cell of the electrolyser thanks '
                   'to the photons which will excite the water molecule and the electrons so that they change '
                   'their atomic orbits until the electrons are released and create the decomposition of water. '
                   '* the decrease in the intensity of the electric current less than or equal to 166.67 mA is '
                   'compensated by the extreme rise in the electric voltage at the level of the electrolyser '
                   'cell (Q = i. t = C. U)')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{i}$'))
        doc.append('be the electric current supplied to the cell in amperes.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{U}$'))
        doc.append('be the electric voltage supplied to the cell in volts.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{Q}$'))
        doc.append('be the charge supplied to the cell in coulombs.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{C}$'))
        doc.append('be the capacity to the cell in farads.')

        doc.append('\n')

        doc.append('Knowing that the cell is a cylindrical capacitor composed of cylindrical stainless steel tubes.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{D_{1}}$'))
        doc.append('be the outside diameter of the outer tube of the cell, the value of which is 1,905 cm.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{D_{2}}$'))
        doc.append('be the outside diameter of the inside tube of the cell, the value of which is 1,27 cm.')

        doc.append('\n')

        doc.append('Let')
        doc.append(NoEscape(r'$\boxed{h}$'))
        doc.append('be the height of the two cell tubes, the value of which is 10.16 cm')

        doc.append('\n')

        doc.append('We have : ')
        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{C=\frac{2*\pi*\epsilon_{water}*h}{\log_e{\frac{R_{2}}{R_{1}}}}}$'))
        doc.append('\n')
        doc.append(NoEscape(r'''
                        $$
                        \boxed{
                        \begin{cases}
                        R_{1} = 6,35 * 10^{-3} \\ 
                        R_{2} = 9,525 * 10^{-3} \\
                        h = 0,1016 \\ 
                        \epsilon_{r} = 80,2 \\
                        \epsilon_{water} = 7 * 10^{-10} \\
                        \epsilon_{vacuum} = 8,8541878128 * 10^{-12} \\
                        C = 1,10209271 * 10^{-9}
                        \end{cases}
                        }
                        $$
                        '''))

        doc.append('\n')
        doc.append(NoEscape(r'$\boxed{h}$'))
        doc.append('is the length of the cylinders in meter ; ')
        doc.append(NoEscape(r'$\boxed{R_{1}}$'))
        doc.append('is the outside radius of the inner cylinder in meter ; ')
        doc.append(NoEscape(r'$\boxed{R_{2}}$'))
        doc.append('is the outside radius of the outside cylinder in meter ; ')
        doc.append(NoEscape(r'$\boxed{\epsilon_{vacuum}}$'))
        doc.append('is the vacuum permittivity in farad per meter ; ')
        doc.append(NoEscape(r'$\boxed{\epsilon_{r}}$'))
        doc.append('is the relative permittivity of the water without unit ; ')
        doc.append(NoEscape(r'$\boxed{\epsilon_{water}}$'))
        doc.append('is the water permittivity ; ')
        doc.append(NoEscape(r'$\boxed{C}$'))
        doc.append('is the capacitance of the capacitor included in the water bath in farad')

        doc.append('\n')
        doc.append('Calculate Q knowing that U = 1000 V.')
        doc.append('We have :')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                Q &= C . U \\
                &= 1,10209271 . 10^{-9} . 10^{3} \\
                &= 1,10209271 . 10^{-6}
                \end{cases}
                }
                $$
                '''
            )
        )
        doc.append('Q is in coulombs.')

        doc.append('\n')

        doc.append('Calculate the number of moles of electrons in the cell in mol.')
        doc.append('\n')
        doc.append('We have :')
        doc.append(NoEscape(r'$\boxed{ Q = n_{e^{-}} . F }$'))
        doc.append('where F is the Faraday constant = 96500 coulombs per mol')
        doc.append('\n')
        doc.append('We have :')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                n_{e^{-}} &= \frac{Q}{F} \\
                &= \frac{ 1,10209271 . 10^{-6} }{ 96500 } \\
                &= 1,14206498 . 10^{-11}
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Calculate the number of electrons in the cell.')
        doc.append('\n')
        doc.append("According to Avogadro's law, we have : ")
        doc.append(NoEscape(r'$\boxed{ N_{i}(X) = n_{i(X)} . N_{A} }$'))
        doc.append("where")
        doc.append(NoEscape(r'$\boxed{ N_{A} }$'))
        doc.append("is the Avogadro constant whose value is : ")
        doc.append(NoEscape(r'$\boxed{ 6,02214076 . 10^{23} }$'))
        doc.append(NoEscape(r'$mol^{-1}.$'))

        doc.append('\n')
        doc.append('We have : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                N(e^{-}) &= n(e^{-}) . N_{A} \\
                &= 1,14206498 . 10^{-11} . 6,02214076 . 10^{23} \\
                &= 6,9 * 10^{12}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence, the number of electrons in the cell is equal to 6.9 trillion electrons.')
        doc.append('\n')
        doc.append('We have : ')
        doc.append(NoEscape(r'$\boxed{ f = \frac{1}{T} \iff T = \frac{1}{f} = \frac{1}{10^{4}} = 10^{-4} }$'))
        doc.append('where f is in Hz and T is in seconds.')
        doc.append('\n')
        doc.append('The cell of the electrolyser receives an alternating current, no negative value.')

        doc.append('\n')
        doc.append('\n')

        doc.append('Classic electrolysis : \n')
        doc.append('')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                * \quad High \quad direct \quad current \\
                * \quad Low \quad electric \quad voltage \\
                * \quad No \quad resonance \quad phenomenon \\
                * \quad f = 60
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('\n')

        doc.append('Stanley Meyer electrolysis : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                * \quad Weak \quad alternating \quad electric \quad current \\
                * \quad High \quad AC \quad voltage \\
                * \quad Resonance \quad phenomenon \\
                * \quad High \quad frequency = 10 kHz \\
                * \quad Duty \quad cyle = 50% \\
                * \quad T_{ON} = 50 * 10^{-6}
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.generate_pdf(clean_tex=True)

    def test_demonstration_for_efficiency_with_pylatex(self):
        doc = Document('efficiency')

        # Preamble of the document
        doc.preamble.append(Command('title', 'US patent n°4,936,961 - Demonstration for efficiency'))
        doc.preamble.append(Command('author', ''))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.preamble.append(Command('usepackage', NoEscape(r'amsmath')))
        doc.preamble.append(Command('usepackage', NoEscape(r'chemfig')))
        doc.preamble.append(Command('usepackage', NoEscape(r'mhchem')))
        doc.append(NoEscape(r'\maketitle'))

        doc.append(NoEscape(r'\underline{Course}'))
        doc.append('\n')
        doc.append('The mass per mol of hydrogen is equal to 1 gramm per mol.')
        doc.append('\n')
        doc.append('Chemical formula for water electrolysis : ')
        doc.append('\n')
        doc.append('Cathode : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \schemestart \ce{2H+} + \ce{2e-} \arrow{->} \ce{H2_{(g)}} \schemestop
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append('Anode : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \schemestart \ce{2H2O_{(l)}} \arrow{->} \ce{O2_{(g)}} + \ce{4H+_{(aq)}} + \ce{4e-} \schemestop
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append('Final reaction : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \schemestart \ce{2H2O_{(l)}} \arrow{->} \ce{O2_{(g)}} + \ce{H2_{(g)}} \schemestop
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('\n')

        doc.append(NoEscape(r'\underline{Calculations}'))
        doc.append('\n')
        doc.append('We have : ')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                M_{H_{2}} = 2 \\
                n_{H_{2}}(t) = \frac{n_{e_{-}}(t)}{2} \\
                m_{H_{2}}(t) = n_{H_{2}}(t) . M_{H_{2}} \\
                PCI_{H_{2}} = 34 \\
                C = 1,10209271 . 10^{-9} \\
                L = 2,03 . 10^{-5} \\
                f = 10^{4} \\
                F = 96500 \\
                T = \frac{1}{f} = 10^{-5} \\
                U_{2} = 78
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(NoEscape(r'\boxed{ F }'))
        doc.append('is the Faraday constant in coulomb per mol ; ')
        doc.append(NoEscape(r'\boxed{U_{2}}'))
        doc.append('is the voltage of the secondary coil of the transformer ; ')
        doc.append(NoEscape(r'\boxed{f}'))
        doc.append('is the frequency of signal in Hz ; ')
        doc.append(NoEscape(r'\boxed{M_{H_{2}}}'))
        doc.append('is the molar mass of the dihydrogen in g per mol ; ')
        doc.append(NoEscape(r'\boxed{PCI_{H_{2}}}'))
        doc.append('is the energy of dihydrogen in kWh per kg ; ')
        doc.append(NoEscape(r'\boxed{n_{e_{-}}}'))
        doc.append('is the quantity of matter of electrons in mol ; ')
        doc.append(NoEscape(r'\boxed{n_{H_{2}}}'))
        doc.append('is the quantity of matter of dihydrogen in mol ; ')
        doc.append(NoEscape(r'\boxed{m_{H_{2}}}'))
        doc.append('is the mass of dihydrogen produced in kg ; ')
        doc.append(NoEscape(r'\boxed{L}'))
        doc.append('is the inductance of the coil in henry ; ')

        doc.append('\n')
        doc.append('\n')
        doc.append('\n')

        doc.append('We are here to resolve any ordinary differential equation with the reel world.')
        doc.append('\n')
        doc.append('\n')
        doc.append('Between 0 and the half of the period, we have the following electronic circuit : ')
        doc.append('\n')
        doc.append('')

        doc.append('\n')

        doc.append('Thanks to the law of voltages, we have : ')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                U_{2} = 2 . U_{L}^{(1)}(t) + U_{C}^{(1)}(t) \iff 78 = 2 . L . 
                \frac{\mathrm d i_{C}^{(1)}(t)}{\mathrm d t} + U_{C}^{(1)}(t) \\
                \iff 78 = 2 . L . C . \frac{\mathrm d^{2} U_{C}^{(1)}(t)}{\mathrm d t^{2}} + U_{C}^{(1)}(t) \\
                \iff \frac{\mathrm d^{2} U_{C}^{(1)}(t)}{\mathrm d t^{2}} 
                + \frac{U_{C}^{(1)}(t)}{2.L.C} - \frac{78}{2.L.C} = 0 \\
                \iff \frac{\mathrm d^{2} U_{C}^{(1)}(t)}{\mathrm d t^{2}} 
                + 22,35.10^{12}.U_{C}^{(1)}(t) - 1,7.10^{15} = 0
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                \alpha = \frac{1}{2.L.C} \\
                \beta = \frac{78}{2.L.C} \\
                \omega = \sqrt{\alpha} \\
                (E):\frac{\mathrm d^{2} U_{C}^{(1)}(t)}{\mathrm d t^{2}} + \alpha.U_{C}^{(1)}(t) = \beta
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('The homogeneous equation : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \frac{\mathrm d^{2} U_{C}^{(1)}(t)}{\mathrm d t^{2}} + \alpha.U_{C}^{(1)}(t) = 0
                }
                $$
                '''
            )
        )
        doc.append('has for solutions : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], U^{(1)}_{C}(t) = 
                \gamma.\cos(\omega.t) + \lambda.\sin(\omega.t)
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(NoEscape(r'\boxed{ \beta }'))
        doc.append('is a polynomial function, so (E) owns a particular solution of the form P where '
                   'P is a polynomial function as the same degree as ')
        doc.append(NoEscape(r'\boxed{ \beta }'))

        doc.append('\n')

        doc.append('Hence,')
        doc.append(NoEscape(r'\boxed{ t \in [0; \frac{T}{2}], P(t) = a }'))
        doc.append('where a ')
        doc.append(NoEscape(r'\boxed{ \in reel. }'))

        doc.append('\n')

        doc.append('Find the value of a in injecting it into (E).')

        doc.append('\n')

        doc.append('P is a particular solution of (E), so : ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                \frac{\mathrm d^{2} P(t)}{\mathrm d t^{2}} + \alpha.P(t) = \beta \iff 0 + a.\alpha = \beta \\
                \iff a = \frac{\beta}{\alpha} = 78
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                t \in [0; \frac{T}{2}], P(t) = 78
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('All solution of (E) is sum of a particular solution of the homogeneous equation associated of '
                   '(E) and a particular solution of (E).')

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], U^{(1)}_{C}(t) = 
                \gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], Q^{(1)}(t) &= C . U^{(1)}_{C}(t) \\
                &= C . (\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], i^{(1)}_{C}(t) 
                &= C . \frac{\mathrm d U_{C}^{(1)}(t)}{\mathrm d t} \\
                &= C . \frac{\mathrm d (\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78) }{\mathrm d t} \\
                &= C . (-\gamma.\omega.\sin(\omega.t) + \lambda.\omega.\cos(\omega.t)) \\
                &= C . \omega . (\lambda.\cos(\omega.t)) -\gamma.\sin(\omega.t))
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], n_{e^{-}}^{(1)}(t) &= \frac{Q^{(1)}(t)}{F} \\
                &= \frac{C . (\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)}{F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], n_{H_{2}}^{(1)}(t) 
                &= \frac{n_{e^{-}}^{(1)}(t)}{2} \\
                &= \frac{C . (\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)}{2.F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], m_{H_{2}}^{(1)}(t) 
                &= n_{H_{2}}^{(1)}(t) . M_{H_{2}} \\
                &= \frac{C . (\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)}{F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], E_{H_{2}}^{(1)}(t) 
                &= PCI_{H_{2}} . m_{H_{2}}^{(1)}(t) \\
                &= \frac{34 . C . (\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)}{F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence, ')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], E_{Transfo}^{(1)}(t) 
                &= U_{2}(t).i_{C}^{(1)}(t).t \\
                &= 78.C.\frac{\mathrm d U_{C}^{(1)}(t)}{\mathrm d t}.t \\
                &= 78.t.C.\omega.(\lambda.\cos(\omega.t)) -\gamma.\sin(\omega.t))
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('\n')
        doc.append('\n')

        doc.append('Between the half of the period and the period, we have the following electronic circuit : ')
        doc.append('\n')
        doc.append('')

        doc.append('\n')
        doc.append('Thanks to the law of voltages, we have : ')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                (E):\frac{\mathrm d^{2} U_{C}^{(1)}(t)}{\mathrm d t^{2}} + U_{C}^{(1)}(t).\alpha = 0
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append('where')
        doc.append(NoEscape(r'$\boxed{\alpha = \frac{1}{(L_{2}+2.L).C}}$'))

        doc.append('\n')

        doc.append('The characteristic equation of the equation (E) is : ')
        doc.append(NoEscape(r'$\boxed{X^{2} + \alpha = 0}$'))

        doc.append('\n')

        doc.append('Let ')
        doc.append(NoEscape(r'$\boxed{ \varDelta }$'))
        doc.append('be the discriminant of the characteristic equation of the equation (E).')

        doc.append('\n')

        doc.append('We have : ')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \varDelta = 0^{2} - 4.1.\alpha < 0
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Let r1 and r2 be the complex roots of the characteristic equation of the equation (E).')

        doc.append('\n')

        doc.append('We have : ')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                r1 = \frac{ -0 -i.\sqrt{ | \varDelta | } }{2.1} = -i.\sqrt{\alpha} \\
                r2 = i.\sqrt{\alpha}
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2}; T], U_{C}^{(2)}(t) = \gamma.\cos(\omega.t) 
                + \lambda.\sin(\omega.t)
                }
                $$
                '''
            )
        )
        doc.append('\n')
        doc.append('where')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \omega = \sqrt{\alpha}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2}; T], Q^{(2)}(t) &= C . U_{C}^{(2)}(t) \\
                &= C . ( \gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) )
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2}; T], i_{C}^{(2)}(t) 
                &= C . \frac{\mathrm d U_{C}^{(2)}(t)}{\mathrm d t} \\
                &= C . \frac{\mathrm d ( \gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) ) }{\mathrm d t} \\
                &= C . (-\gamma.\omega.\sin(\omega.t) + \lambda.\omega.\cos(\omega.t)) \\
                &= C . \omega . ( \lambda.\cos(\omega.t) - \gamma.\sin(\omega.t) )
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2}; T], n_{e^{-}}^{(2)}(t) &= \frac{Q^{(2)}(t)}{F} \\
                &= \frac{C . ( \gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) )}{F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2}; T], n_{H_{2}}^{(2)}(t) 
                &= \frac{ n_{e^{-}}^{(2)}(t) }{2} \\
                &= \frac{C . ( \gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) ) }{2.F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2}; T], m_{H_{2}}^{(2)}(t) 
                &= n_{H_{2}}^{(2)}(t) . M_{H_{2}} \\
                &= \frac{ C.(\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t)).2}{2.F} \\
                &= \frac{C.(\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t)) }{F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2}; T], E_{H_{2}}^{(2)}(t) 
                &= PCI_{H_{2}} . m_{H_{2}}^{(2)}(t) \\
                &= \frac{34.C.(\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t))}{F}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                t \in [\frac{T}{2}; T], E_{Transfo}^{(2)}(t) &= U_{2}(t).i_{C}^{(2)}(t).t \\
                &= 0.i_{C}^{(2)}(t).t \\
                &= 0
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [0; \frac{T}{2}], \eta^{(1)}(t) 
                &= \frac{ E_{H_{2}}^{(1)}(t) }{ E_{Transfo}^{(1)}(t) } \\
                &= \frac{ \frac{34 . C . (\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)}{F} }
                { 78.t.C.\omega.(\lambda.\cos(\omega.t)) -\gamma.\sin(\omega.t)) } \\
                &= \frac{34.C.(\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)}
                {F.78.t.C.\omega.(\lambda.\cos(\omega.t)) -\gamma.\sin(\omega.t))} \\
                &= \frac{17.(\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t) + 78)}
                {39.F.t.\omega.(\lambda.\cos(\omega.t)) -\gamma.\sin(\omega.t))}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, t \in [\frac{T}{2} ; T], \eta^{(2)}(t)
                &= \frac{ E_{H_{2}}^{(2)}(t) }{ E_{Transfo}^{(2)}(t) } \\
                &= \frac{ \frac{34.C.(\gamma.\cos(\omega.t) + \lambda.\sin(\omega.t))}{F} }{ 0 } \\
                &= \infty
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')
        doc.append('Hence,')
        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                (\gamma, \lambda) \in reel, \eta^{(1)}(t = \frac{T}{2}) 
                &= \frac{ 17.(\gamma.\cos(\omega.\frac{T}{2}) + \lambda.\sin(\omega.\frac{T}{2}) + 78) }
                {39.F.\frac{T}{2}.\omega.( \lambda.\cos(\omega.\frac{T}{2}) - \gamma.\sin(\omega.\frac{T}{2}) )} \\
                &= \frac{ 17.(\gamma.\cos(\frac{2.\pi.T}{T.2}) + \lambda.\sin(\frac{2.\pi.T}{T.2}) + 78) }
                { 39.F.\frac{T.2.\pi}{2.T}.(\lambda.\cos(\frac{2.\pi.T}{T.2}) - \gamma.\sin(\frac{2.\pi.T}{T.2})) } \\
                &= \frac{17.(-\gamma + 78)}{39.F.\pi.(-\lambda)} \\
                &= \frac{17.(78 - \gamma)}{39.F.\pi.\lambda}
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('We are here to resolve any ordinary differential equation with the imaginary world '
                   'or the complex number world.')

        doc.append('\n')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                Equation (1) ; U_{C}^{(1)}(t=0)
                &= 0 \\
                &= \gamma.cos(\omega.0) + \lambda..sin(\omega.0) + 78 \\
                &= \gamma + 78
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                Equation (1) ; \gamma = - 78
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                Equation (1) ; i^{(1)}_{C}(t = 0) = 0 
                &= C . \omega . (\lambda.\cos(\omega.0)) -\gamma.\sin(\omega.0)) \\
                &= C . \omega . \lambda . 1
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                Equation (1) ; \lambda = 0 ; \gamma = - 78
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                Equation (1) ; \lambda = 0 ; \gamma = - 78 \\
                t \in [0; \frac{T}{2}], U_{C}^{(1)}(t) = 78.(1 - cos(\omega.t)) \\
                t \in [0; \frac{T}{2}], Q^{(1)}(t) = C.78.(1 - cos(\omega.t)) \\
                t \in [0; \frac{T}{2}], i^{(1)}_{C}(t) = C.\omega.78.sin(\omega.t) \\
                t \in [0; \frac{T}{2}], n_{e^{-}}^{(1)} = \frac{C.78.(1-cos(\omega.t))}{F} \\
                t \in [0; \frac{T}{2}], n_{H_{2}}^{(1)}(t) = \frac{C.78.(1-cos(\omega.t))}{2.F} \\
                t \in [0; \frac{T}{2}], m_{H_{2}}^{(1)}(t) = \frac{C.78.(1-cos(\omega.t))}{F} \\
                t \in [0; \frac{T}{2}], E_{H_{2}}^{(1)}(t) = \frac{34.C.78.(1-cos(\omega.t))}{F} \\
                t \in [0; \frac{T}{2}], E_{Transfo}^{(1)}(t) = (78)^{2}.t.C.\omega.sin(\omega.t) \\
                t \in [0; \frac{T}{2}], \eta^{(1)}(t) = \frac{1326.(1 - cos(\omega.t)}{3042.F.t.\omega.sin(\omega.t)}
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                Equation (2) \\
                U_{C}^{(2)}(t = \frac{T}{2}) = U_{C}^{(1)}(t = \frac{T}{2}) = 156 &\iff \gamma.(-1) = 156 \\
                &\iff \gamma = - 156
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                Equation (2) \\
                i_{C}^{(2)}(t = \frac{T}{2}) = i_{C}^{(1)}(t = \frac{T}{2}) = 0 &\iff C.\omega.\lambda.(-1) = 0 \\
                &\iff \lambda = 0
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                Equation (2) ; \lambda = 0 ; \gamma = -156 \\
                t \in [\frac{T}{2}, T], U_{C}^{(2)}(t) = -156.cos(\omega.t) \\
                t \in [\frac{T}{2}, T], Q^{(2)}(t) = -156.C.cos(\omega.t) \\
                t \in [\frac{T}{2}, T], i^{(2)}_{C}(t) = 156.C.\omega.sin(\omega.t) \\
                t \in [\frac{T}{2}, T], n_{e^{-}}^{(2)}(t) = \frac{-156.C.cos(\omega.t)}{F} \\
                t \in [\frac{T}{2}, T], n_{H_{2}}^{(2)}(t) = \frac{-156.C.cos(\omega.t)}{2.F} \\
                t \in [\frac{T}{2}, T], m_{H_{2}}^{(2)}(t) = \frac{-156.C.cos(\omega.t)}{F} \\
                t \in [\frac{T}{2}, T], E_{H_{2}}^{(2)}(t) = \frac{-5304.C.cos(\omega.t)}{F} \\
                t \in [\frac{T}{2}, T], E_{Transfo}^{(2)}(t) = 0 \\
                t \in [\frac{T}{2}, T], \eta^{(2)}(t) = \infty
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{aligned}
                m_{H_{2}}^{(1)}(t = \frac{T}{2}) &= \frac{156.C}{F} \\
                &= 1,781.10^{-12} kg \\
                \end{aligned}
                }
                $$
                '''
            )
        )

        doc.append('\n')

        doc.append('I prefer to reduce the problem.')
        doc.append(
            NoEscape(
                r'''
                $$
                \boxed{
                \begin{cases}
                m_{H_{2}}^{(total)}(t \in [0, T]) = 1,781.10^{-12} kg \\
                m_{H_{2}}^{(total)}(t \in [0, x.T]) = x.1,781.10^{-12} kg \\
                \end{cases}
                }
                $$
                '''
            )
        )

        doc.generate_pdf(clean_tex=True)

    def test_demonstration_for_Uc1_for_efficiency_with_pylatex(self):
        # Uc is a function of t
        f = Function("f")(x)

        # f1 is the first derivative of f
        f1 = Derivative(f, x)

        # f2 is the first derivative of f1
        f2 = Derivative(f1, x)

        # eq is the equation described the Uc(t) between 0 and T/2 in the circuit
        eq = Eq(f2 - 22.35*(10**12)*f, - 1.7*(10**15))

        #hint
        hint = "nth_linear_constant_coeff_variation_of_parameters, " \
               "nth_linear_constant_coeff_undetermined_coefficients ," \
               "nth_linear_constant_coeff_variation_of_parameters_Integral"

        pprint(dsolve(eq=eq, func=f, hint="default", simplify=True))

    def test_demonstration_for_Uc2_for_efficiency_with_pylatex(self):
        # f is a function of t
        f = Function("f")(x)

        # f1 is the first derivative of f
        f1 = Derivative(f, x)

        # f2 is the first derivative of f1
        f2 = Derivative(f1, x)

        # eq is the equation described the Uc(t) between 0 and T/2 in the circuit
        eq = f2 + f1

        hint = ''

        pprint(dsolve(eq, func=f, hint=hint))

    def test_demonstration_with_quantum_mechanic(self):
        doc = Document('quantum_mechanics')

        # Preamble of the document
        doc.preamble.append(Command('title', 'US patent n°4,936,961 - Demonstration from quantum mechanics'))
        doc.preamble.append(Command('author', ''))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.preamble.append(Command('usepackage', NoEscape(r'amsmath')))
        doc.append(NoEscape(r'\maketitle'))

        doc.append(NoEscape(r'\underline{Course}'))

        doc.append('\n')

        doc.generate_pdf(clean_tex=True)

    def test_electronic_simulation(self):
        # Circuit
        mycir = ahkab.Circuit('Voltage Intensifier Circuit')

        # Get the ref node (gnd)
        gnd = mycir.get_ground_node()

        # Pulse train source
        pulse_train = time_functions.pulse(v1=0, v2=26, td=0, tr=0, tf=0, pw=50e-6, per=100e-6)
        mycir.add_vsource('V1', n1='n1', n2=gnd, dc_value=26, ac_value=26, function=pulse_train)

        # Primary winding of the transformer
        mycir.add_inductor(part_id="L1T", n1="n1", n2=gnd, value=0.004536)

        # Secondary winding of the transformer
        mycir.add_inductor(part_id="L2T", n1="n2", n2=gnd, value=0.040824)

        # Transformer
        mycir.add_inductor_coupling(part_id="K1", L1="L1T", L2="L2T", value=1)

        # Model of the diode
        mycir.add_model(
            model_type="diode",
            model_label="Diode_1N1198",
            model_parameters=dict(IS=0.167, N=1.0, ISR=0, NR=2.0, RS=0)
        )

        # Diode 1N1198
        mycir.add_diode(
            part_id="D1",
            n1="n2",
            n2="n3",
            model_label="Diode_1N1198"
        )

        # First inductor
        mycir.add_inductor(part_id="L1", n1="n3", n2="n4", value=2.03e-5)

        # Capacitor
        mycir.add_capacitor(part_id="C1", n1="n4", n2="n5", value=1.10209271e-9)

        # Second inductor
        mycir.add_inductor(part_id="L2", n1="n5", n2=gnd, value=2.03e-5)

        # Print the circuit
        #print(mycir)

        # Type of analysis
        op_analysis = ahkab.new_op()
        ac_analysis = ahkab.new_ac(start=1e3, stop=1e5, points=100)
        tran_analysis = ahkab.new_tran(tstart=0, tstop=1.2e-3, tstep=1e-6, x0=None)

        # Run
        r = ahkab.run(mycir, an_list=[op_analysis, ac_analysis, tran_analysis])

        print(r)

    def test_electronic_simulation_example(self):
        mycir = ahkab.Circuit('Simple Example Circuit')

        mycir.add_resistor('R1', 'n1', mycir.gnd, value=5)
        mycir.add_vsource('V1', 'n2', 'n1', dc_value=8)
        mycir.add_resistor('R2', 'n2', mycir.gnd, value=2)
        mycir.add_vsource('V2', 'n3', 'n2', dc_value=4)
        mycir.add_resistor('R3', 'n3', mycir.gnd, value=4)
        mycir.add_resistor('R4', 'n3', 'n4', value=1)
        mycir.add_vsource('V3', 'n4', mycir.gnd, dc_value=10)
        mycir.add_resistor('R5', 'n2', 'n4', value=4)

        opa = ahkab.new_op()
        r = ahkab.run(mycir, opa)['op']

        print(r)


class UnitTestsDSIBSMBUS4936961WithMatplotlib(unittest.TestCase):
    # ok
    def test_simple_plot(self):
        print("test_simple_plot")

        # Data for plotting
        t = np.arange(0.0, 2.0, 0.01)

        s = 1 + math.pow(1/2, 1/4) * math.pow(4, 1/4) * math.pow(1 / 100, 1 / 4) * np.sin(2 * np.pi * t)

        fig, ax = plt.subplots()

        ax.plot(t, s)

        ax.set(
            xlabel='time (s)',
            ylabel='voltage (mV)',
            title='About as simple as it gets, folks'
        )

        ax.grid()

        fig.savefig("test.png")

        plt.show()

    # ok
    def test_plot_uc1(self):
        print('test_plot_uc1')

        # The inductance of the coil
        L = 1.8*math.pow(10, -4)

        # The capacitance of the capacitor
        C = 4.1 * math.pow(10, -5)

        # The vibration of the LC electronic circuit
        omega = 1/(math.sqrt(2*L*C))

        # The period of the LC electronic circuit
        T = (2*math.pi)/omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 200

        # The number of turns of the secondary coil of the transformer
        N_2_T = 600

        # The main voltage source
        U_source = 230

        print('T/2 : ' + str(T/2))

        t = np.arange(0.0, T/2, 1*math.pow(10, -8))

        u_c_1 = (1/2) * (N_2_T/N_1_T) * U_source * (np.sin(omega * t) - omega * t * np.cos(omega * t))

        fig, ax = plt.subplots()

        ax.plot(t, u_c_1)

        ax.set(
            xlabel='Time (s)',
            ylabel='Voltage (V)',
            title='The voltage U_c_1(t) across the capacitor during the period [0, T/2]'
        )

        ax.grid()

        fig.savefig("plot_u_c_1.png")

        plt.show()

    # ok
    def test_plot_uc2(self):
        print('test_plot_uc2')

        # The inductance of the coil
        L = 1.8*math.pow(10, -4)

        # The capacitance of the capacitor
        C = 7.59*math.pow(10, -9)

        # The vibration of the LC electronic circuit
        omega = 1/(math.sqrt(2*L*C))

        # The period of the LC electronic circuit
        T = (2*math.pi)/omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 200

        # The number of turns of the secondary coil of the transformer
        N_2_T = 600

        # The main voltage source
        U_source = 230

        print('T/2 : ' + str(T/2))

        t = np.arange(T/2, T, 1*math.pow(10, -9))

        u_c_2 = (-1) * (np.pi/2) * (N_2_T/N_1_T) * U_source * np.cos(omega * t)

        fig, ax = plt.subplots()

        ax.plot(t, u_c_2)

        ax.set(
            xlabel='Time (s)',
            ylabel='Voltage (V)',
            title='The voltage U_c_2(t) across the capacitor during the period [T/2, T]'
        )

        ax.grid()

        fig.savefig("plot_u_c_2.png")

        plt.show()

    # ok
    def test_plot_vh1(self):
        print('test_plot_vh1')

        # The inductance of the coil
        L = 1.8*math.pow(10, -4)

        # The capacitance of the capacitor
        C = 4.1*math.pow(10, -5)

        # The vibration of the LC electronic circuit
        omega = 1/(math.sqrt(2*L*C))

        # The period of the LC electronic circuit
        T = (2*math.pi)/omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 200

        # The number of turns of the secondary coil of the transformer
        N_2_T = 600

        # The main voltage source
        U_source = 230

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 0.082

        # The Faraday constant in coulomb per mol
        F = 96500

        print('T/2 : ' + str(T/2))

        t = np.arange(0.0, T/2, 1*math.pow(10, -5))

        v_h_1 = (Mh2/rho_h2) * (C/F) * (1/2) * (N_2_T/N_1_T) * U_source * (np.sin(omega * t) - omega * t * np.cos(omega * t))

        fig, ax = plt.subplots()

        ax.plot(t, v_h_1)

        ax.set(
            xlabel='Time (s)',
            ylabel='Cubic meter (m^3)',
            title='The volume of dihydrogen v_h_1(t) \n during the period [0, T/2]'
        )

        ax.grid()

        fig.savefig("plot_v_h_1.png")

        plt.show()

    # ok
    def test_plot_vh2(self):
        print('test_plot_vh2')

        # The inductance of the coil
        L = 1.8*math.pow(10, -4)

        # The capacitance of the capacitor
        C = 7.59*math.pow(10, -9)

        # The vibration of the LC electronic circuit
        omega = 1/(math.sqrt(2*L*C))

        # The period of the LC electronic circuit
        T = (2*math.pi)/omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 200

        # The number of turns of the secondary coil of the transformer
        N_2_T = 600

        # The main voltage source
        U_source = 230

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 0.082

        # The Faraday constant in coulomb per mol
        F = 96500

        print('T/2 : ' + str(T/2))

        t = np.arange(T/2, T, 1*math.pow(10, -9))

        v_h_2 = (Mh2/rho_h2) * (C/F) * (-1) * (np.pi/2) * (N_2_T/N_1_T) * U_source * np.cos(omega * t)

        fig, ax = plt.subplots()

        ax.plot(t, v_h_2)

        ax.set(
            xlabel='Time (s)',
            ylabel='Cubic meter (m^3)',
            title='The volume of dihydrogen v_h_2(t) \n during the period [T/2, T]'
        )

        ax.grid()

        fig.savefig("plot_v_h_2.png")

        plt.show()

    # ok
    def test_plot_flow_rate_hydrogen_from_voltage_without_tesla_coils(self):
        print('test_plot_flow_rate_hydrogen_from_voltage_without_tesla_coils')

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The capacitance of the capacitor
        C = 2.73 * math.pow(10, -7)

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 2 * math.pow(10, 2)

        # The number of turns of the secondary coil of the transformer
        N_2_T = 2 * math.pow(10, 6)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 0.082

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # axe x
        voltage = np.arange(0, 2.3*math.pow(10, 2), math.pow(10, 1))

        # The total volume of dihydrogen produced in cubic meter during the operation of the Stanley Meyer water
        # electrolyser
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) * (N_2_T/N_1_T) * (voltage/np.pi)

        # axe y
        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)

        fig, ax = plt.subplots()

        ax.plot(voltage, g_f_r_h2)

        ax.set(
            xlabel='Applied voltage (V)',
            ylabel='Cubic meter per hour (m^3/h)',
            title='The flow rate of dihydrogen for one hydrogen generator by using one \n '
                  'electrical transformer with a ratio of 10000'
        )

        ax.grid()

        fig.savefig("plot_flow_rate_from_voltage_without_tesla_coils.png")

        plt.show()

    # ok
    def test_plot_flow_rate_hydrogen_from_voltage_with_tesla_coils(self):
        print('test_plot_flow_rate_hydrogen_from_voltage_with_tesla_coils')

        # The number of steps of Tesla coils
        number_of_steps_of_tesla_coils = 8

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The capacitance of the capacitor
        C = 2.73 * math.pow(10, -7)

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the Tesla transformer
        N_1_T = 10

        # The number of turns of the secondary coil of the Tesla transformer
        N_2_T = math.pow(10, 3)

        # The radius of the secondary coil of the Tesla transformer
        R_2_T = math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        R_1_T = R_2_T + math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        l_1 = 2.5 * math.pow(10, -3) * N_1_T

        # The radius of the secondary coil of the Tesla transformer
        l_2 = 0.511 * math.pow(10, -3) * N_2_T

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # axe x
        voltage = np.arange(0, math.pow(10, 4), math.pow(10, 2))

        # The total volume of dihydrogen produced in cubic meter during the operation of hydrogen production
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) \
                     * math.pow(N_2_T/N_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(R_2_T/R_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(l_1/l_2, number_of_steps_of_tesla_coils/2) \
                     * (voltage/np.pi)

        # axe y
        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)

        fig, ax = plt.subplots()

        ax.plot(voltage, g_f_r_h2)

        ax.set(
            xlabel='Applied voltage (V)',
            ylabel='Cubic meter per hour (m^3/h)',
            title='The flow rate of dihydrogen for one hydrogen generator by using '
                  + str(number_of_steps_of_tesla_coils)
                  + ' \n Tesla coils with a ratio of 100 in series'
        )

        ax.grid()

        fig.savefig(
            "plot_flow_rate_from_voltage_with_"
            + str(number_of_steps_of_tesla_coils)
            + "_tesla_coils_in_series.png"
        )

        plt.show()

    # ok
    def test_plot_radius_hydrogen_tube(self):
        print('test_plot_radius_hydrogen_tube')

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The maximal pressure into the gas tube
        p_h2 = 90 * math.pow(10, 5)

        # axe x
        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = np.arange(0, 20, 1)

        # axe y
        # The minimum radius of the gas tube
        r_gas_tube = math.pow(1/2, 1/4) * math.pow(rho_h2, 1/4) * math.pow(1 / p_h2, 1 / 4) \
                     * np.power(g_f_r_h2/np.pi, 1/2)

        fig, ax = plt.subplots()

        ax.plot(g_f_r_h2, r_gas_tube)

        ax.set(
            xlabel='Flow rate of dihydrogen (m^3/h)',
            ylabel='Radius of the hydrogen tube (m)',
            title='The radius of the hydrogen tube in function of the flow rate of dihydrogen \n '
                  'for one hydrogen generator'
        )

        ax.grid()

        fig.savefig(
            "plot_radius_hydrogen_tube_from_flow_rate_dihydrogen.png"
        )

        plt.show()


class UnitTestsDSIBSMBUS4936961ForCalculusHydrogenGenerationWithoutTeslaCoilsInSteps(unittest.TestCase):
    # ok
    def test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_generator_without_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_generator_without_tesla_coils_in_steps')

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The capacitance of the capacitor
        C = 2.73 * math.pow(10, -7)

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 2 * math.pow(10, 2)

        # The number of turns of the secondary coil of the transformer
        N_2_T = 6 * math.pow(10, 2)

        # The main voltage source
        U_source = 2.3 * math.pow(10, 2)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 0.082

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of the Stanley Meyer water
        # electrolyser
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) * (N_2_T/N_1_T) * (U_source/np.pi)

        print('The total volume of dihydrogen produced during the operation of one hydrogen genrator '
              'is equal to : ' + str(v_h2_total) + ' cubic meters.')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour of one hydrogen generator.')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour of one hydrogen generator.')

    # ok
    def test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_rack_without_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_rack_without_tesla_coils_in_steps')

        # The number of hydrogen generator on one rack
        number_of_hydrogen_generator_on_one_rack = 15

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The total capacitance of the equivalent capacitor
        C = number_of_hydrogen_generator_on_one_rack * (2.73 * math.pow(10, -7))

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 2 * math.pow(10, 2)

        # The number of turns of the secondary coil of the transformer
        N_2_T = 6 * math.pow(10, 2)

        # The main voltage source
        U_source = 10 * math.pow(10, 3)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of the Stanley Meyer water
        # electrolyser
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) * (N_2_T/N_1_T) * (U_source/np.pi)
        print('The total volume of dihydrogen produced during the operation of one hydrogen rack '
              'is equal to : ' + str(v_h2_total) + ' cubic meters.')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour for one hydrogen rack.')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour of one hydrogen generator.')

    # ok
    def test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_container_without_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_container_without_tesla_coils_in_steps')

        # The number of hydrogen rack in one container
        number_of_hydrogen_rack_in_one_container = 10

        # The number of hydrogen generator on one rack
        number_of_hydrogen_generator_on_one_rack = 15

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The total capacitance of the equivalent capacitor
        C = number_of_hydrogen_rack_in_one_container * number_of_hydrogen_generator_on_one_rack \
            * (2.73 * math.pow(10, -7))

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 2 * math.pow(10, 2)

        # The number of turns of the secondary coil of the transformer
        N_2_T = 6 * math.pow(10, 2)

        # The main voltage source
        U_source = 10 * math.pow(10, 3)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of the Stanley Meyer water
        # electrolyser
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) * (N_2_T/N_1_T) * (U_source/np.pi)

        print('The total volume of dihydrogen produced during the operation of one hydrogen container '
              'is equal to : ' + str(v_h2_total) + ' cubic meters.')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour for one hydrogen container.')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour of one hydrogen generator.')

    # ok
    def test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_plant_without_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_flow_rate_for_one_hydrogen_plant_without_tesla_coils_in_steps')

        # The surface of one hydrogen container in square meter
        surface_hydrogen_container = 15

        # The total surface of the operation site of the industrial plant
        surface_operation_site = 500

        # The number of hydrogen container in one plant
        number_of_hydrogen_container_in_one_plant = round(surface_operation_site/surface_hydrogen_container)

        # The number of hydrogen rack in one container
        number_of_hydrogen_rack_in_one_container = 10

        # The number of hydrogen generator on one rack
        number_of_hydrogen_generator_on_one_rack = 15

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The total capacitance of the equivalent capacitor
        C = number_of_hydrogen_container_in_one_plant * number_of_hydrogen_rack_in_one_container * \
            number_of_hydrogen_generator_on_one_rack * (2.73 * math.pow(10, -7))

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the transformer
        N_1_T = 2 * math.pow(10, 2)

        # The number of turns of the secondary coil of the transformer
        N_2_T = 6 * math.pow(10, 2)

        # The main voltage source
        U_source = 10 * math.pow(10, 3)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of the Stanley Meyer water
        # electrolyser
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) * (N_2_T/N_1_T) * (U_source/np.pi)

        print('The total volume of dihydrogen produced during the operation of one hydrogen container '
              'is equal to : ' + str(v_h2_total) + ' cubic meters.')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour for one hydrogen container.')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour of one hydrogen generator.')


class UnitTestsDSIBSMBUS4936961ForCalculusHydrogenGenerationWithTeslaCoilsInSteps(unittest.TestCase):
    # ok
    def test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_generator_with_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_generator_with_tesla_coils_in_steps')

        # The number of steps of Tesla coils
        number_of_steps_of_tesla_coils = 8

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The capacitance of the capacitor
        C = 2.73 * math.pow(10, -7)

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the Tesla transformer
        N_1_T = 10

        # The number of turns of the secondary coil of the Tesla transformer
        N_2_T = math.pow(10, 3)

        # The radius of the secondary coil of the Tesla transformer
        R_2_T = math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        R_1_T = R_2_T + math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        l_1 = 2.5 * math.pow(10, -3) * N_1_T

        # The radius of the secondary coil of the Tesla transformer
        l_2 = 0.511 * math.pow(10, -3) * N_2_T

        # The main voltage source passed through the neon transformer
        U_source = math.pow(10, 4)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of hydrogen production
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) \
                     * math.pow(N_2_T/N_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(R_2_T/R_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(l_1/l_2, number_of_steps_of_tesla_coils/2) \
                     * (U_source/np.pi)

        print('The total volume of dihydrogen produced during the operation of one hydrogen generator '
              'is equal to : ' + str(v_h2_total) + ' cubic meters in one day. \n')

        print('The total volume of dihydrogen produced during the operation of one hydrogen generator '
              'is equal to : ' + str(v_h2_total * 365) + ' cubic meters in one year. \n')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour. \n')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour.')

        # The maximal pressure into the gas tube
        p_h2 = 90 * math.pow(10, 5)

        # The minimum radius of the gas tube
        r_gas_tube = math.pow(1/2, 1/4) \
                     * math.pow(rho_h2, 1/4) \
                     * math.pow(g_f_r_h2/np.pi, 1/2) \
                     * math.pow(1/p_h2, 1/4)

        print("The minimum radius of the gas tube is equal to : " + str(r_gas_tube) + " in meter.")

    # ok
    def test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_rack_with_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_rack_with_tesla_coils_in_steps')

        # The number of steps of Tesla coils
        number_of_steps_of_tesla_coils = 7

        # The number of hydrogen generator on one rack
        number_of_hydrogen_generator_on_one_rack = 15

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The total capacitance of the equivalent capacitor
        C = number_of_hydrogen_generator_on_one_rack * (2.73 * math.pow(10, -7))

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the Tesla transformer
        N_1_T = 10

        # The number of turns of the secondary coil of the Tesla transformer
        N_2_T = math.pow(10, 3)

        # The radius of the secondary coil of the Tesla transformer
        R_2_T = math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        R_1_T = R_2_T + math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        l_1 = 2.5 * N_1_T

        # The radius of the secondary coil of the Tesla transformer
        l_2 = 0.511 * N_2_T

        # The main voltage source passed through the neon transformer
        U_source = math.pow(10, 4)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of hydrogen production
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) \
                     * math.pow(N_2_T/N_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(R_2_T/R_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(l_1/l_2, number_of_steps_of_tesla_coils/2) \
                     * (U_source/np.pi)

        print('The total volume of dihydrogen produced during the operation of one hydrogen rack '
              'is equal to : ' + str(v_h2_total) + ' cubic meters in one day. \n')

        print('The total volume of dihydrogen produced during the operation of one hydrogen rack '
              'is equal to : ' + str(v_h2_total * 365) + ' cubic meters in one year. \n')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour for one hydrogen rack.')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour.')

        # The maximal pressure into the gas tube
        p_h2 = 95 * math.pow(10, 5)

        # The minimum radius of the gas tube
        r_gas_tube = math.pow(1/2, 1/4) \
                     * math.pow(rho_h2, 1/4) \
                     * math.pow(g_f_r_h2/np.pi, 1/2) \
                     * math.pow(1/p_h2, 1/4)

        print("The minimum radius of the gas tube is equal to : " + str(r_gas_tube) + " in meter.")

    # ok
    def test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_container_with_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_container_with_tesla_coils_in_steps')

        # The number of steps of Tesla coils
        number_of_steps_of_tesla_coils = 10

        # The number of hydrogen rack in one container
        number_of_hydrogen_rack_in_one_container = 5

        # The number of hydrogen generator on one rack
        number_of_hydrogen_generator_on_one_rack = 15

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The total capacitance of the equivalent capacitor
        C = number_of_hydrogen_rack_in_one_container * number_of_hydrogen_generator_on_one_rack \
            * (2.73 * math.pow(10, -7))

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the Tesla transformer
        N_1_T = 10

        # The number of turns of the secondary coil of the Tesla transformer
        N_2_T = math.pow(10, 3)

        # The radius of the secondary coil of the Tesla transformer
        R_2_T = math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        R_1_T = R_2_T + math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        l_1 = 2.5 * N_1_T

        # The radius of the secondary coil of the Tesla transformer
        l_2 = 0.511 * N_2_T

        # The main voltage source passed through the neon transformer
        U_source = math.pow(10, 4)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of hydrogen production
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) \
                     * math.pow(N_2_T/N_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(R_2_T/R_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(l_1/l_2, number_of_steps_of_tesla_coils/2) \
                     * (U_source/np.pi)

        print('The total volume of dihydrogen produced during the operation of one hydrogen container '
              'is equal to : ' + str(v_h2_total) + ' cubic meters in one day. \n')

        print('The total volume of dihydrogen produced during the operation of one hydrogen container '
              'is equal to : ' + str(v_h2_total * 365) + ' cubic meters in one year. \n')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour.')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour.')

        # The maximal pressure into the gas tube
        p_h2 = 95 * math.pow(10, 5)

        # The minimum radius of the gas tube
        r_gas_tube = math.pow(1/2, 1/4) \
                     * math.pow(rho_h2, 1/4) \
                     * math.pow(g_f_r_h2/np.pi, 1/2) \
                     * math.pow(1/p_h2, 1/4)

        print("The minimum radius of the gas tube is equal to : " + str(r_gas_tube) + " in meter.")

    # ok
    def test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_plant_with_tesla_coils_in_steps(self):
        print('test_total_volume_dihydrogen_produced_and_other_variables_for_one_hydrogen_plant_with_tesla_coils_in_steps')

        # The number of steps of Tesla coils
        number_of_steps_of_tesla_coils = 10

        # The number of hydrogen container in one plant
        number_of_hydrogen_container_in_one_plant = 1

        # The number of hydrogen rack in one container
        number_of_hydrogen_rack_in_one_container = 5

        # The number of hydrogen generator on one rack
        number_of_hydrogen_generator_on_one_rack = 15

        # The inductance of the coil
        L = 1.44 * math.pow(10, -3)

        # The total capacitance of the equivalent capacitor
        C = number_of_hydrogen_container_in_one_plant * number_of_hydrogen_rack_in_one_container * \
            number_of_hydrogen_generator_on_one_rack * (2.73 * math.pow(10, -7))

        # The vibration of the LC electronic circuit
        omega = 1 / (math.sqrt(2 * L * C))

        # The period of the LC electronic circuit
        T = (2 * math.pi) / omega

        # The number of turns of the primary coil of the Tesla transformer
        N_1_T = 10

        # The number of turns of the secondary coil of the Tesla transformer
        N_2_T = math.pow(10, 3)

        # The radius of the secondary coil of the Tesla transformer
        R_2_T = math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        R_1_T = R_2_T + math.pow(10, -2)

        # The radius of the primary coil of the Tesla transformer
        l_1 = 2.5 * N_1_T

        # The radius of the secondary coil of the Tesla transformer
        l_2 = 0.511 * N_2_T

        # The main voltage source passed through the neon transformer
        U_source = math.pow(10, 4)

        # The molar mass of dihydrogen in kg per mol
        Mh2 = 2.0 * math.pow(10, -3)

        # The volumic mass of dihydrogen in kg per cubic meter
        rho_h2 = 70.973

        # The Faraday constant in coulomb per mol
        F = 96500

        # The time of the operation of the Stanley Meyer water electrolyser in seconds.
        t_f = 24*60*60

        # The total volume of dihydrogen produced in cubic meter during the operation of hydrogen production
        v_h2_total = (t_f/T) * (Mh2/rho_h2) * (C/F) \
                     * math.pow(N_2_T/N_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(R_2_T/R_1_T, number_of_steps_of_tesla_coils) \
                     * math.pow(l_1/l_2, number_of_steps_of_tesla_coils/2) \
                     * (U_source/np.pi)

        print('The total volume of dihydrogen produced during the operation of one hydrogen container '
              'is equal to : ' + str(v_h2_total) + ' cubic meters in one day. \n')

        print('The total volume of dihydrogen produced during the operation of one hydrogen container '
              'is equal to : ' + str(v_h2_total * 365) + ' cubic meters in one year. \n')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour
        g_f_r_h2 = (v_h2_total/3600)

        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2)
              + ' cubic meter per hour for one hydrogen container. \n')

        # The dihydrogen flow rate during the operation time t_f in cubic meter per hour for each hydrogen generator
        g_f_r_h2_h_g = (g_f_r_h2/(number_of_hydrogen_container_in_one_plant * number_of_hydrogen_rack_in_one_container
                        * number_of_hydrogen_generator_on_one_rack))
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_h_g)
              + ' cubic meter per hour for one hydrogen generator. \n')

        # The dihydrogen flow rate during the operation time t_f in kilograms per hour
        g_f_r_h2_kg = (v_h2_total/3600) * rho_h2
        print('The dihydrogen flow rate during the operation time t_f is equal to : ' + str(g_f_r_h2_kg)
              + ' kilograms per hour.')

        # The maximal pressure into the gas tube
        p_h2 = 95 * math.pow(10, 5)

        # The minimum radius of the gas tube
        r_gas_tube = math.pow(1/2, 1/4) \
                     * math.pow(rho_h2, 1/4) \
                     * math.pow(g_f_r_h2/np.pi, 1/2) \
                     * math.pow(1/p_h2, 1/4)

        print("The minimum radius of the gas tube is equal to : " + str(r_gas_tube) + " in meter.")


if __name__ == '__main__':
    unittest.main()
