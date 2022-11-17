import unittest
import pdfkit
from datetime import datetime as dt
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class Statuts(unittest.TestCase):
    # ok
    def test_statuts_mercorus(self):
        print("test_statuts_mercorus")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        
            <title>Les statuts de la société MERCORUS</title>
          </head>
          <body>
            <div class="card text-center">
              <div class="card-header">
                Les statuts de la société MERCORUS
              </div>
              <div class="card-body">
                <!-- Informations générales de la société MERCORUS -->
                <div class="card text-center">
                  <div class="card-header">
                    Informations générales de la société MERCORUS
                  </div>
                  <div class="card-body">
                    MERCORUS
                    <br>
                    Société par actions simplifiée unipersonnelle à capital variable au capital social de 100,00 euros
                    <br>
                    Siège social : 
                  </div>
                </div>
                <!-- Informations générales de la société MERCORUS -->
                
                <br>
                <br>
                
                <!-- Responsable de la rédaction -->
                <div class="card text-center">
                  <div class="card-header">
                    Responsable de la rédaction des statuts de la société MERCORUS
                  </div>
                  <div class="card-body">
                    Je soussigné Monsieur  né le  à 
                    Saint-Louis (97450) demeurant au  Étage 1 – Porte 6 93800 Épinay-sur-Seine 
                    de nationalité française a établi ainsi qu'il suit les statuts de la société MERCORUS, 
                    société par actions simplifiée unipersonnelle à capital variable qu'il a décidé d'instituer.
                  </div>
                </div>
                <!-- Responsable de la rédaction -->
                
                <br>
                <br>
                
                <!-- Abréviations -->
                <div class="card text-center">
                  <div class="card-header">
                    Abréviations
                  </div>
                  <div class="card-body">
                    L'abréviation «S.A.S.U.A.C.V.» veut dire «Société par actions simplifiée unipersonnelle à 
                    capital variable». 
                    <br>
                    L'abréviation «S.A.S.A.C.V.» veut dire «Société par actions simplifiée à capital variable».
                  </div>
                </div>
                <!-- Abréviations -->
                
                <br>
                <br>
                
                <!-- TITRE I : FORME JURIDIQUE / OBJET / DENOMINATION SOCIALE / SIEGE SOCIAL / DUREE -->
                <div class="card text-center">
                  <div class="card-header">
                    TITRE I : FORME JURIDIQUE / OBJET / DENOMINATION SOCIALE / SIEGE SOCIAL / DUREE
                  </div>
                  <div class="card-body">
                    <h6>Vu les articles L210-1 à L210-12 du code de commerce,</h6>
                    
                    <br>
                    <br>
                    
                    <!-- Article 1 – Forme juridique -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 1 – Forme juridique
                      </div>
                      <div class="card-body">
                        La société MERCORUS est une société par actions simplifiée unipersonnelle à capital variable 
                        régie par les dispositions légales et réglementaires en vigueur selon
                        les articles L227-1 à L227-20 du code de commerce concernant les sociétés par
                        actions simplifiées et les articles L231-1 à L231-8 du code de commerce concernant
                        le capital variable et par les présents statuts.
                      </div>
                    </div>
                    <!-- Article 1 – Forme juridique -->
                
                    <br>
                    <br>
                    
                    <!-- Article 2 – Objet social -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 2 – Objet social
                      </div>
                      <div class="card-body">
                        <h6>
                            La S.A.S.U.A.C.V. MERCORUS a pour objet social directement ou indirectement, en France et 
                            à l'étranger :
                            
                            <br>
                            
                            - la production de métaux précieux;
                            
                            <br>
                            <br>
                            
                            - le commerce de gros (commerce interentreprises) de minerais et métaux;
                            
                            <br>
                            <br>
                            
                            - la participation de la S.A.S.U.A.C.V. MERCORUS, par tous moyens, à toutes entreprises 
                            ou sociétés créées ou à créer, pouvant se rattacher à l'objet social, notamment par 
                            voie de création de sociétés nouvelles, d'apport, commandite, souscription ou rachat de 
                            titres ou droits sociaux, fusion, alliance ou association en participation ou groupement 
                            d'intérêt économique ou de location gérance ;
                            
                            <br>
                            <br>
                            
                            - et plus généralement, toutes opérations industrielles, commerciales et financières, 
                            mobilières et immobilières pouvant se rattacher directement ou indirectement à l'objet 
                            social et à tous objets similaires ou connexes pouvant favoriser son extension ou son 
                            développement.
                        </h6>
                      </div>
                    </div>
                    <!-- Article 2 – Objet social -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 3 - Dénomination sociale -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 3 - Dénomination sociale
                      </div>
                      <div class="card-body">
                        La dénomination sociale de la S.A.S.U.A.C.V. est : MERCORUS.
                        
                        <br>
                        <br>
                        
                        Tous les actes, devis, factures, annonces, publications et autres documents 
                        émanant de la S.A.S.U.A.C.V. MERCORUS doivent indiquer la dénomination 
                        sociale, précédée ou suivie immédiatement des mots « société par actions simplifiée 
                        unipersonnelle à capital variable » ou des initiales « S.A.S.U.A.C.V. » et de 
                        l'énonciation du montant du capital social.
                      </div>
                    </div>
                    <!-- Article 3 - Dénomination sociale  -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 4 - Siège social -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 4 - Siège social
                      </div>
                      <div class="card-body">
                        Le siège social de la S.A.S.U.A.C.V. MERCORUS est fixé au : .
                        
                        <br>
                        <br>
                        
                        Le siège social de la S.A.S.U.A.C.V. MERCORUS détermine notamment la loi 
                        applicable et la compétence des juridictions en cas de litiges survenus entre les tiers 
                        et la S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        Le siège social de la S.A.S.U.A.C.V. MERCORUS peut être transféré dans le
                        même département ou dans un département limitrophe par décision de l'associé 
                        unique de la S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        Le siège social de la S.A.S.U.A.C.V. MERCORUS peut être transféré en tout 
                        autre endroit par décision de l'associé unique de la S.A.S.U.A.C.V. MERCORUS.
                      </div>
                    </div>
                    <!-- Article 4 - Siège social -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 5 – Durée -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 5 – Durée
                      </div>
                      <div class="card-body">
                        La S.A.S.U.A.C.V. MERCORUS est constituée pour une durée de QUATRE-VINGT-DIX-NEUF ans qui 
                        commence à courir à compter du jour de son immatriculation au Registre des Commerces et des 
                        Sociétés sauf cas de dissolution anticipée ou prorogation par décision de l’associé unique de 
                        la S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        Cette durée peut être prorogée, une ou plusieurs fois, par décision de l'associé 
                        unique de la S.A.S.U.A.C.V. MERCORUS sans que cette prorogation puisse 
                        excéder QUATRE-VINGT-DIX-NEUF ans.
                        
                        <br>
                        <br>
                        
                        En vertu des articles R210-14 à R210-15 du code de commerce concernant la
                        dissolution de la société, les décisions de dissolution anticipée de la 
                        S.A.S.U.A.C.V. MERCORUS sont prises dans les mêmes formes que celles indiquées ci-dessus 
                        par décision de l’associé unique de la S.A.S.U.A.C.V. MERCORUS.
                      </div>
                    </div>
                    <!-- Article 5 – Durée -->
                  </div>
                </div>
                <!-- TITRE I : FORME JURIDIQUE / OBJET / DENOMINATION SOCIALE / SIEGE SOCIAL / DUREE -->
                
                <br>
                <br>
                
                <!-- TITRE II : APPORTS / CAPITAL SOCIAL / FORME DES ACTIONS / LIBERATION DES ACTIONS / 
                TRANSMISSION ET INDIVISIBILITE DES ACTIONS / DROITS ET OBLIGATIONS ATTACHES AUX ACTIONS -->
                <div class="card text-center">
                  <div class="card-header">
                    TITRE II : APPORTS / CAPITAL SOCIAL / FORME DES ACTIONS / LIBERATION DES ACTIONS / TRANSMISSION ET INDIVISIBILITE DES ACTIONS / DROITS ET OBLIGATIONS ATTACHES AUX ACTIONS
                  </div>
                  <div class="card-body">
                    <!-- Article 6 – Apports -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 6 – Apports
                      </div>
                      <div class="card-body">
                        L'associé unique de la S.A.S.U.A.C.V. MERCORUS, soussigné Monsieur Jason
                        Aymérick Jean Claudius ALOYAU, né le  à Saint-Louis (97450),
                        demeurant au  Étage 1 - Porte 6 93800 Épinay-sur-Seine, a fait
                        les apports suivants à la S.A.S.U.A.C.V. MERCORUS:
                        
                        <br>
                        
                        - La somme en numéraire de CENT euros, ci 100,00 euros, correspondant à 50
                        actions de 2,00 euros, souscrites en totalité et libérées intégralement, a été
                        déposée sur un compte ouvert au nom de la Caisse des dépôts et
                        consignations, conformément aux dispositions de la loi n°2001-420 du 15 mai
                        2001, pour le compte de la S.A.S.U.A.C.V. MERCORUS en cours
                        d’immatriculation.
                      </div>
                    </div>
                    <!-- Article 6 – Apports -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 7 - Capital social -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 7 - Capital social
                      </div>
                      <div class="card-body">
                        Le montant du capital social souscrit de la S.A.S.U.A.C.V. MERCORUS est fixé à
                        la somme de CENT euros, ci 100,00 euros, divisé en 50 actions de 2,00 euros
                        chacune, de même catégorie, numérotées de 1 à 50, entièrement libérées,
                        appartenant à l'associé unique de la S.A.S.U.A.C.V. MERCORUS.
                      </div>
                    </div>
                    <!-- Article 7 - Capital social -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 8 - Modifications du capital social -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 8 - Modifications du capital social
                      </div>
                      <div class="card-body">
                        Le montant du capital social de la S.A.S.U.A.C.V. MERCORUS peut être
                        augmenté ou réduit dans les conditions prévues par les articles L231-1 à L231-8 du
                        code de commerce par décision de l'associé unique de la S.A.S.U.A.C.V.
                        MERCORUS.
                        
                        <br>
                        <br>
                        
                        <!-- Clause planché -->
                        <div class="card text-center">
                          <div class="card-header">
                            Clause planché
                          </div>
                          <div class="card-body">
                            Le montant du capital social de la S.A.S.U.A.C.V. MERCORUS pourra être 
                            abaissé dans la limite de VINGT euros, ci 20 euros.
                          </div>
                        </div>
                        <!-- Clause planché -->
                        
                        <br>
                        <br>
                        
                        <!-- Clause plafond -->
                        <div class="card text-center">
                          <div class="card-header">
                            Clause plafond
                          </div>
                          <div class="card-body">
                            Le montant du capital social de la S.A.S.U.A.C.V. MERCORUS ne pourra pas
                            être augmenté d’un BILLIARD d’euros, ci 1 000 000 000 000 000,00 euros sans
                            respecter les formalités de modification des statuts conformément aux articles R123-
                            105 à R123-110 du code de commerce.
                          </div>
                        </div>
                        <!-- Clause plafond -->
                      </div>
                    </div>
                    <!-- Article 8 - Modifications du capital social -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 9 - Forme des actions -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 9 - Forme des actions
                      </div>
                      <div class="card-body">
                        Vu les articles L228-7 à L228-29-7 du code de commerce concernant les actions,
                        
                        <br>
                        <br>
                        
                        En application des articles L228-1 à L228-6-3 du code de commerce, les actions
                        émises par la S.A.S.U.A.C.V. MERCORUS consenties par décision de l’associé
                        unique de la S.A.S.U.A.C.V. MERCORUS sont obligatoirement nominatives et
                        inscrites au nom de leur titulaire sur des comptes et registres tenus à cet effet par la
                        S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        Les actions nominatives émises par la S.A.S.U.A.C.V. MERCORUS consenties
                        par l’associé unique de la S.A.S.U.A.C.V. MERCORUS ne peuvent pas être
                        converties en actions au porteur.
                        
                        <br>
                        <br>
                        
                        En vertu de l’article L228-8 du code de commerce, le montant nominal des actions
                        ou coupures d'action émises par la S.A.S.U.A.C.V. MERCORUS consenties par
                        l’associé unique de la S.A.S.U.A.C.V. MERCORUS est fixé à la somme de DEUX
                        euros, ci 2,00 euros.
                      </div>
                    </div>
                    <!-- Article 9 - Forme des actions -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 10 - Libération des actions émises par la S.A.S.U. à capital variable MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 10 - Libération des actions émises par la S.A.S.U. à capital variable MERCORUS
                      </div>
                      <div class="card-body">
                        Vu l'article L228-7 du code de commerce concernant les actions,
                        
                        <br>
                        <br>
                        
                        Lors d'une augmentation de capital social de la S.A.S.U.A.C.V. MERCORUS, les
                        actions de numéraire de la S.A.S.U.A.C.V. MERCORUS sont libérées, lors de la
                        souscription, de la moitié de leur valeur nominale et, le cas échéant, de la totalité de
                        la prime d'émission.
                        
                        <br>
                        <br>
                        
                        La libération du surplus doit intervenir en une ou plusieurs fois sur appel du
                        Président de la S.A.S.U.A.C.V. MERCORUS, dans le délai de CINQ ans à
                        compter de l'immatriculation au Registre du Commerce et des Sociétés en ce qui
                        concerne le capital social initial de la S.A.S.U.A.C.V. MERCORUS, et dans le
                        délai de CINQ ans à compter du jour où l'opération est devenue définitive en cas
                        d'augmentation de capital social de la S.A.S.U.A.C.V. MERCORUS.
                      </div>
                    </div>
                    <!-- Article 10 - Libération des actions émises par la S.A.S.U. à capital variable MERCORUS -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 11 - Transmission, location et indivisibilité des actions émises par la 
                    S.A.S.U. à capital variable MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 11 - Transmission, location et indivisibilité des actions émises par la S.A.S.U. 
                        à capital variable MERCORUS
                      </div>
                      <div class="card-body">
                        Vu l’alinéa 4 de l’article L227-1 du code de commerce concernant les modalités de
                        souscription et de répartition des actions d’une société par actions,
                        
                        <br>
                        <br>
                        
                        Vu les articles L228-1 à L228-6-3 du code de commerce concernant les dispositions
                        communes aux valeurs mobilières,
                        
                        <br>
                        <br>
                        
                        Vu les articles L228-7 à L228-29-7 du code de commerce concernant les actions,
                        
                        <br>
                        <br>
                        
                        Vu les articles L239-1 à L239-5 du code de commerce concernant la location
                        d'actions et de parts sociales,
                        
                        <br>
                        <br>
                        
                        Vu les articles R228-1 à R228-14 du code de commerce concernant les dispositions
                        communes des valeurs mobilières émises par les sociétés par actions,
                        
                        <br>
                        <br>
                        
                        Vu l’article R228-23 du code de commerce concernant les clauses d'agrément de la
                        cession de titres de capital ou de valeurs mobilières donnant accès au capital,
                        
                        <br>
                        <br>
                        
                        Vu l’article R239-1 du code de commerce concernant la location d'actions et de parts
                        sociales,
                        
                        <br>
                        <br>
                        
                        Vu les articles 639, 653, 662-3° et 726 du code général des impôts,
                        
                        <br>
                        <br>
                        
                        <!-- Transmission -->
                        <div class="card text-center">
                          <div class="card-header">
                            Transmission
                          </div>
                          <div class="card-body">
                            Dans le respect des règles de l’article L228-10 du code de commerce, les actions
                            émises par la S.A.S.U.A.C.V. MERCORUS consenties par l'associé unique de la
                            S.A.S.U.A.C.V. MERCORUS sont librement négociables.
                            
                            <br>
                            <br>
                                
                            Les transmissions d'actions émises par la S.A.S.U.A.C.V. MERCORUS
                            consenties par l'associé unique de la S.A.S.U.A.C.V. MERCORUS s'effectuent
                            librement.
                            
                            <br>
                            <br>
                            
                            Les transmissions d’actions émises par la S.A.S.U.A.C.V. MERCORUS
                            consenties par l'associé unique de la S.A.S.U.A.C.V. MERCORUS s'opèrent à
                            l'égard de la S.A.S.U.A.C.V. MERCORUS et des tiers par virement du compte du
                            cédant au compte du cessionnaire sur production d’une copie de la signature d’un
                            ordre de mouvement accompli par le formulaire CERFA n°2759-SD signé par le
                            cédant et le cessionnaire, une copie d’une pièce d’identité du cessionnaire et un
                            justificatif d’adresse du cessionnaire tel que la facture d’électricité, la facture d’eau
                            ou la facture de téléphone envoyés par lettre recommandée avec demande d'avis de
                            réception à l’adresse du siège social de la S.A.S.U.A.C.V. MERCORUS et
                            affranchie dans un délai de huit jours à compter de la date de l’ordre de mouvement.
                            
                            <br>
                            <br>
                            
                            Toute transmission d’action émise par la S.A.S.U.A.C.V. MERCORUS consentie
                            par l'associé unique de la S.A.S.U.A.C.V. MERCORUS qui n’est pas opérée à
                            l’égard de la S.A.S.U.A.C.V. MERCORUS est réputée caduque.
                          </div>
                        </div>
                        <!-- Transmission -->
                        
                        <br>
                        <br>
                        
                        <!-- Location -->
                        <div class="card text-center">
                          <div class="card-header">
                            Location
                          </div>
                          <div class="card-body">
                            Les actions émises par la S.A.S.U.A.C.V. MERCORUS peuvent être données en
                            location à une personne physique au respect des articles L239-1 à L239-5 du code
                            de commerce concernant la location d'actions et de parts sociales.
                            
                            <br>
                            <br>
                            
                            Tant que la S.A.S.U.A.C.V. MERCORUS sera une société par actions simplifiée
                            unipersonnelle et que les transmissions d'actions émises par la S.A.S.U.A.C.V.
                            MERCORUS seront libres, le locataire des actions émises par la S.A.S.U.A.C.V.
                            MERCORUS consenties par l’associé unique de la S.A.S.U.A.C.V.
                            MERCORUS n'a pas à être agréé.
                            
                            <br>
                            <br>
                            
                            Si la S.A.S.U.A.C.V. MERCORUS perd son caractère unipersonnel, alors le
                            Locataire des actions émises par la S.A.S.A.C.V. MERCORUS devra être agréé
                            dans les conditions qui seront éventuellement prévues dans la clause d’agrément de
                            cession d’actions définie dans les statuts de la S.A.S.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            Dans ce cas, le refus d'agrément du Locataire fera obstacle à la location effective
                            des actions émises par la S.A.S.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            La location des actions émises par la S.A.S.U.A.C.V. MERCORUS n'est
                            opposable à la S.A.S.U.A.C.V. MERCORUS que si le contrat de location des
                            actions émises par la S.A.S.U.A.C.V. MERCORUS, établi par acte sous seing
                            privé et soumis à la formalité de l'enregistrement fiscal ou établi par acte
                            authentique, a été signifié par acte extrajudiciaire à la S.A.S.U.A.C.V.
                            MERCORUS ou si ledit contrat a été accepté par l’associé unique de la
                            S.A.S.U.A.C.V. MERCORUS dans un acte authentique.
                            
                            <br>
                            <br>
                            
                            La résiliation du contrat de location des actions émises par la S.A.S.U.A.C.V.
                            MERCORUS par le Locataire des actions émises par la S.A.S.U.A.C.V.
                            MERCORUS consenties par l’associé unique de la S.A.S.U.A.C.V.
                            MERCORUS doit être notifiée à la S.A.S.U.A.C.V. MERCORUS par lettre
                            recommandée avec demande d’avis de réception à l’adresse du siège social de la
                            S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            La résiliation du contrat de location des actions émises par la S.A.S.U.A.C.V.
                            MERCORUS par la S.A.S.U.A.C.V. MERCORUS doit être notifiée au
                            Locataire des actions émises par la S.A.S.U.A.C.V. MERCORUS consenties par
                            l’associé unique de la S.A.S.U.A.C.V. MERCORUS par lettre recommandée avec
                            demande d’avis de réception à l’adresse du domicile du locataire des actions émises
                            par la S.A.S.U.A.C.V. MERCORUS consenties par l’associé unique de la
                            S.A.S.U.A.C.V. MERCORUS dans le cas d’une personne physique ou à l’adresse
                            du siège social du locataire des actions émises par la S.A.S.U.A.C.V. 
                            MERCORUS consenties par l’associé unique de la S.A.S.U.A.C.V.
                            MERCORUS dans le cas d’une personne morale.
                            
                            <br>
                            <br>
                            
                            La résiliation du contrat de location des actions émises par la S.A.S.U.A.C.V.
                            MERCORUS par la S.A.S.U.A.C.V. MERCORUS peut être exécutée à tout
                            moment par les deux parties en vertu du deuxième alinéa de l’article L239-4 du code
                            de commerce.
                            
                            <br>
                            <br>
                            
                            En cas de renouvellement du bail des actions émises par la S.A.S.U.A.C.V.
                            MERCORUS consenties par l’associé unique de la S.A.S.U.A.C.V.
                            MERCORUS, le bail est renouvelé dans les mêmes conditions que la conclusion
                            du bail initial des actions émises par la S.A.S.U.A.C.V. MERCORUS consenties
                            par l’associé unique de la S.A.S.U.A.C.V. MERCORUS en vertu du premier
                            alinéa de l’article L239-4 du code de commerce.
                            
                            <br>
                            <br>
                            
                            La délivrance des actions louées par la S.A.S.U.A.C.V. MERCORUS au locataire
                            des actions émises par la S.A.S.U.A.C.V. MERCORUS consenties par l’associé
                            unique de la S.A.S.U.A.C.V. MERCORUS est réalisée à la date à laquelle est
                            inscrite, dans le registre des titres nominatifs de la S.A.S.U.A.C.V. MERCORUS,
                            à côté du nom de l’associé unique de la S.A.S.U.A.C.V. MERCORUS, la mention
                            du bail des actions émises par la S.A.S.U.A.C.V. MERCORUS consenties par
                            l’associé unique de la S.A.S.U.A.C.V. MERCORUS et du nom du locataire des
                            actions émises par la S.A.S.U.A.C.V. MERCORUS consenties par l’associé
                            unique de la S.A.S.U.A.C.V. MERCORUS. 
                            
                            <br>
                            <br>
                            
                            À compter de la date de délivrance des actions louées par la S.A.S.U.A.C.V. 
                            MERCORUS au locataire consenties par l’associé unique de la S.A.S.U.A.C.V. MERCORUS, 
                            la S.A.S.U.A.C.V. MERCORUS doit adresser au locataire les informations dues aux 
                            actionnaires ou associés et prévoir sa participation et son droit de vote aux assemblées
                            conformément aux dispositions du deuxième alinéa de l’article L239-3 du code de
                            commerce.
                            
                            <br>
                            <br>
                            
                            Cette mention du bail des actions émises par la S.A.S.U.A.C.V.
                            MERCORUS consenties par l’associé unique de la S.A.S.U.A.C.V.
                            MERCORUS sera supprimée du registre des mouvement de titres nominatifs de la
                            S.A.S.U.A.C.V. MERCORUS dès que la résiliation du contrat de location des
                            actions émises par la S.A.S.U.A.C.V. MERCORUS consenties par l’associé
                            unique de la S.A.S.U.A.C.V. MERCORUS aura été signifiée à la S.A.S.U.A.C.V.
                            MERCORUS en vertu du deuxième alinéa de l’article L239-4 du code de
                            commerce.
                            
                            <br>
                            <br>
                            
                            Les actions émises par la S.A.S.U.A.C.V. MERCORUS consenties par l’associé
                            unique de la S.A.S.U.A.C.V. MERCORUS faisant l'objet d’une location doivent
                            être évaluées en débuts et en fin de contrat, ainsi qu'à la fin de chaque exercice
                            comptable de la S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            Cette évaluation sera effectuée sur la base de critères tirés des comptes sociaux 
                            de la S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            Cette évaluation sera certifiée par un commissaire aux comptes désignée par l’associé 
                            unique de la S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            Conformément à l’article L239-3 du code de commerce, le droit de vote attaché à
                            l'action louée par la S.A.S.U.A.C.V. MERCORUS appartient à l’associé unique de 
                            la S.A.S.U.A.C.V. MERCORUS dans les assemblées statuant sur les
                            modifications statutaires ou le changement de nationalité de la S.A.S.U.A.C.V.
                            MERCORUS et au locataire dans les autres assemblées.
                            
                            <br>
                            <br>
                            
                            Pour toutes les autres décisions, le droit de vote et les autres droits attachés aux
                            actions louées par la S.A.S.U.A.C.V. MERCORUS, et notamment le droit aux
                            dividendes, sont exercés par le locataire, comme s'il était usufruitier des actions
                            émises par la S.A.S.U.A.C.V. MERCORUS consenties par l’associé unique de la
                            S.A.S.U.A.C.V. MERCORUS, l’associé unique de la S.A.S.U.A.C.V.
                            MERCORUS en étant considéré comme le nu-propriétaire.
                            
                            <br>
                            <br>
                            
                            Pour l'application des dispositions du livre IV du code de commerce, le bailleur et le
                            locataire sont considérés comme détenteurs d'actions émises par la S.A.S.U.A.C.V.
                            MERCORUS consenties par l’associé unique de la S.A.S.U.A.C.V.
                            MERCORUS.
                            
                            <br>
                            <br>
                            
                            À peine de nullité, les actions louées de la S.A.S.U.A.C.V. MERCORUS ne
                            peuvent en aucun cas faire l'objet d'une sous-location ou d'un prêt de titres
                            financiers au sens des articles L211-22 à L211-26 du code monétaire et financier.
                            
                            <br>
                            <br>
                            
                            Conformément à l’article L239-5 du code de commerce, tout intéressé peut
                            demander au président du tribunal de commerce statuant en référé d'enjoindre sous
                            astreinte au Président de la S.A.S.U.A.C.V. MERCORUS, en cas de signification
                            ou d'arrivée à terme d'un contrat de bail portant sur des actions louées de la
                            S.A.S.U.A.C.V. MERCORUS, de modifier le registre des mouvements de titres nominatifs ou les
                            statuts et de convoquer l'assemblée des associés à cette fin.
                          </div>
                        </div>
                        <!-- Location -->
                        
                        <br>
                        <br>
                        
                        <!-- Indivisibilité -->
                        <div class="card text-center">
                          <div class="card-header">
                            Indivisibilité
                          </div>
                          <div class="card-body">
                            Les actions émises par la S.A.S.U.A.C.V. MERCORUS consenties par l’associé
                            unique de la S.A.S.U.A.C.V MERCORUS sont indivisibles à l'égard de la S.A.S.U.
                            A.C.V. MERCORUS conformément à l’article L228-5 du code de commerce.
                          </div>
                        </div>
                        <!-- Indivisibilité -->
                      </div>
                    </div>
                    <!-- Article 11 - Transmission, location et indivisibilité des actions émises par la 
                    S.A.S.U. à capital variable MERCORUS -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 12 - Droits et obligations attachés aux actions émises par la S.A.S.U. à capital 
                    variable MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 12 - Droits et obligations attachés aux actions émises par la S.A.S.U. à capital 
                        variable MERCORUS
                      </div>
                      <div class="card-body">
                        <!-- Droits et obligations -->
                        <div class="card text-center">
                          <div class="card-header">
                            Droits et obligations
                          </div>
                          <div class="card-body">
                            Les associés de la S.A.S.U.A.C.V. MERCORUS ne sont responsables du passif
                            social qu'à concurrence de leurs apports au capital social de la S.A.S.U.A.C.V.
                            MERCORUS.
                            
                            <br>
                            <br>
                            
                            La propriété d'une action émise par la S.A.S.U.A.C.V. MERCORUS consentie par
                            l’associé unique de la S.A.S.U.A.C.V. MERCORUS comporte de plein droit
                            adhésion aux statuts de la S.A.S.U.A.C.V. MERCORUS, aux décisions de la
                            collectivité des associés de la S.A.S.U.A.C.V. MERCORUS et à la participation
                            aux assemblées des associés de la S.A.S.U.A.C.V. MERCORUS sur justification
                            de son identité et de la propriété de ses actions inscrites en compte de la
                            S.A.S.U.A.C.V. MERCORUS depuis au moins 5 jours et libérées des versements
                            exigibles.
                            
                            <br>
                            <br>
                            
                            Les droits et obligations suivent l'action émise par la S.A.S.U.A.C.V. MERCORUS
                            consentie par l’associé unique de la S.A.S.U.A.C.V. MERCORUS quelle qu'en
                            soit le titulaire.
                            
                            <br>
                            <br>
                            
                            Chaque fois qu'il sera nécessaire de posséder plusieurs actions de la
                            S.A.S.U.A.C.V. MERCORUS pour exercer un droit quelconque, en cas
                            d'échange, de regroupement ou d'attribution de titres de la S.A.S.U.A.C.V.
                            MERCORUS ou en conséquence d'augmentation ou de réduction de capital
                            social de la S.A.S.U.A.C.V. MERCORUS, de fusion ou autre opération sociale
                            pour le compte de la S.A.S.U.A.C.V. MERCORUS, les associés propriétaires de
                            titres isolés de la S.A.S.U.A.C.V. MERCORUS, ou en nombre inférieur à celui
                            requis, ne peuvent exercer ces droits qu'à la condition de faire leur affaire
                            personnelle du groupement, et éventuellement de l'achat ou de la vente du nombre
                            d'actions ou droits nécessaires à l'égard de la S.A.S.U.A.C.V. MERCORUS.
                          </div>
                        </div>
                        <!-- Droits et obligations -->
                        
                        <br>
                        <br>
                        
                        <!-- Droit de vote -->
                        <div class="card text-center">
                          <div class="card-header">
                            Droit de vote
                          </div>
                          <div class="card-body">
                            Le droit de vote attaché aux actions de capital social ou de jouissance de la
                            S.A.S.U.A.C.V. MERCORUS est proportionnel à la quotité du capital social de la
                            S.A.S.U.A.C.V. MERCORUS qu'elles représentent et chaque action de la
                            S.A.S.U.A.C.V. MERCORUS donne droit à une voix au moins.
                          </div>
                        </div>
                        <!-- Droit de vote -->
                        
                        <br>
                        <br>
                        
                        <!-- Droits aux bénéfices -->
                        <div class="card text-center">
                          <div class="card-header">
                            Droits aux bénéfices
                          </div>
                          <div class="card-body">
                            Toute action de la S.A.S.U.A.C.V. MERCORUS en l'absence de catégories
                            d'actions, ou toute action de la S.A.S.U.A.C.V. MERCORUS d'une même
                            catégorie d'actions, dans le cas contraire, donne droit à une part nette
                            proportionnelle à la quotité du capital social de la S.A.S.U.A.C.V. MERCORUS
                            qu'elle représente dans les bénéfices et réserves ou dans l'actif social lors de toute
                            distribution, amortissement ou répartition, au cours de la vie de la S.A.S.U.A.C.V.
                            MERCORUS, comme en cas de liquidation, ceci dans les conditions et modalités
                            par ailleurs stipulées dans les présents statuts, le cas échéant, et pour parvenir à ce
                            résultat, il est fait masse de toutes exonérations fiscales comme de toutes taxations
                            pouvant être prises en charge par la S.A.S.U.A.C.V. MERCORUS auxquelles ces
                            distributions, amortissements ou répartitions pourraient donner lieu.
                          </div>
                        </div>
                        <!-- Droits aux bénéfices -->
                      </div>
                    </div>
                    <!-- Article 12 - Droits et obligations attachés aux actions émises par la S.A.S.U. à capital 
                    variable MERCORUS -->                
                  </div>
                </div>
                <!-- TITRE II : APPORTS / CAPITAL SOCIAL / FORME DES ACTIONS / LIBERATION DES ACTIONS / 
                TRANSMISSION ET INDIVISIBILITE DES ACTIONS / DROITS ET OBLIGATIONS ATTACHES AUX ACTIONS -->
                
                <br>
                <br>
                
                <!-- TITRE III - ADMINISTRATION ET DIRECTION DE LA SOCIETE / CONVENTIONS ENTRE LA SOCIETE ET SON 
                    DIRIGEANT / COMMISSAIRES AUX COMPTES -->
                <div class="card text-center">
                  <div class="card-header">
                    TITRE III - ADMINISTRATION ET DIRECTION DE LA SOCIETE / CONVENTIONS ENTRE LA SOCIETE ET SON 
                    DIRIGEANT / COMMISSAIRES AUX COMPTES
                  </div>
                  <div class="card-body">
                    <!-- Article 13 - Président de la S.A.S.U. à capital variable MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 13 - Président de la S.A.S.U. à capital variable MERCORUS
                      </div>
                      <div class="card-body">
                        Vu l’article L227-6 du Code de commerce,
                        
                        <br>
                        <br>
                        
                        La S.A.S.U.A.C.V. MERCORUS est représentée à l'égard des tiers, dirigée et
                        administrée par un Président, personne physique et associé unique de la
                        S.A.S.U.A.C.V. MERCORUS, nommé Monsieur Jason Aymérick Jean Claudius
                        ALOYAU, né le  à Saint-Louis (97450), demeurant au 6 Avenue
                        Léon Blum Étage 1 – Porte 6 93800 Épinay-sur-Seine.
                        
                        <br>
                        <br>
                        
                        L'actionnaire unique de la S.A.S.U.A.C.V. MERCORUS peut nommer un tiers à la
                        présidence de la S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        <!-- Désignation du Président -->
                        <div class="card text-center">
                          <div class="card-header">
                            Désignation du Président
                          </div>
                          <div class="card-body">
                            La S.A.S.U.A.C.V. MERCORUS est représentée à l'égard des tiers par un
                            Président qui est soit une personne physique salariée ou non, associée ou non de la
                            S.A.S.U.A.C.V. MERCORUS, soit une personne morale associée ou non de la
                            S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            Lorsqu'une personne morale est nommée Président de la S.A.S.U.A.C.V.
                            MERCORUS, ses dirigeants sont soumis aux mêmes conditions et obligations de
                            la fonction de Président de la S.A.S.U.A.C.V. MERCORUS et encourent les
                            mêmes responsabilités civile et pénale que s'ils étaient Président en leur propre
                            nom, sans préjudice de la responsabilité solidaire de la personne morale qu'ils
                            dirigent.
                            
                            <br>
                            <br>
                            
                            Le Président de la S.A.S.U.A.C.V. MERCORUS est désigné par décision de
                            l'actionnaire unique de la S.A.S.U.A.C.V. MERCORUS qui fixe son éventuelle
                            rémunération.
                          </div>
                        </div>
                        <!-- Désignation du Président -->
                        
                        <br>
                        <br>
                        
                        <!-- Rémunération du Président -->
                        <div class="card text-center">
                          <div class="card-header">
                            Rémunération du Président
                          </div>
                          <div class="card-body">
                            Le Président de la S.A.S.U.A.C.V. MERCORUS peut recevoir une rémunération
                            en compensation de la responsabilité et de la charge attachées à ses fonctions dont
                            les modalités de fixation et de règlement sont déterminées par une décision de
                            l'associé unique de la S.A.S.U.A.C.V. MERCORUS délibérant dans les conditions
                            prévues pour les décisions ordinaires.
                            
                            <br>
                            <br>
                            
                            En outre, le Président de la S.A.S.U.A.C.V. MERCORUS est remboursé de ses
                            frais de représentation et de déplacement sur justification intervenu dans le cadre de
                            ses fonctions pour le compte de la S.A.S.U.A.C.V. MERCORUS.
                          </div>
                        </div>
                        <!-- Rémunération du Président -->
                        
                        <br>
                        <br>
                        
                        <!-- Durée des fonctions du Président -->
                        <div class="card text-center">
                          <div class="card-header">
                            Durée des fonctions du Président
                          </div>
                          <div class="card-body">
                            Le Président de la S.A.S.U.A.C.V. MERCORUS est nommé pour une durée
                            indéterminée à compter de la date de sa nomination par décision de l’actionnaire
                            unique de la S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            En cas de décès, démission ou empêchement du Président de la S.A.S.U.A.C.V.
                            MERCORUS d'exercer ses fonctions pendant une durée supérieure à 2 mois, un
                            président remplaçant est désigné par décision de l'actionnaire unique de la
                            S.A.S.U.A.C.V. MERCORUS pour la durée du mandat restant à courir.
                          </div>
                        </div>
                        <!-- Durée des fonctions du Président -->
                        
                        <br>
                        <br>
                        
                        <!-- Cessation des fonctions du Président -->
                        <div class="card text-center">
                          <div class="card-header">
                            Cessation des fonctions du Président
                          </div>
                          <div class="card-body">
                            Le Président de la S.A.S.U.A.C.V. MERCORUS peut démissionner sans avoir à
                            justifier de sa décision à condition de notifier celle-ci à l'associé unique de la
                            S.A.S.U. à capital variable MERCORUS, par lettre recommandée avec accusé de
                            réception à l’adresse du siège social de la S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            Un préavis d’une semaine devra être accompli avant le départ définitif du Président de
                            la S.A.S.U.A.C.V. MERCORUS afin d’aborder le rapport de gestion du Président
                            de la S.A.S.U.A.C.V. MERCORUS établissant un état des lieux de la situation
                            globale de la S.A.S.U.A.C.V. MERCORUS, des activités en matière de recherche
                            et développement de la S.A.S.U.A.C.V. MERCORUS, et de l’évolution prévisible
                            de la S.A.S.U.A.C.V. MERCORUS à court terme.
                            
                            <br>
                            <br>
                            
                            L'associé unique de la S.A.S.U.A.C.V. MERCORUS peut mettre fin à tout
                            moment au mandat du Président de la S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            La révocation n'a pas à être motivée. La S.A.S.U.A.C.V. MERCORUS enverra une
                            lettre recommandée avec avis de réception au domicile ou au siège social du
                            Président de la S.A.S.U.A.C.V. MERCORUS pour notifier la révocation du
                            mandat de Président de la S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            Le Président de la S.A.S.U.A.C.V. MERCORUS sera considéré démissionnaire à
                            la date où il aura atteint l’âge de 80 ans révolus.
                          </div>
                        </div>
                        <!-- Cessation des fonctions du Président -->
                        
                        <br>
                        <br>
                        
                        <!-- Pouvoirs du Président -->
                        <div class="card text-center">
                          <div class="card-header">
                            Pouvoirs du Président
                          </div>
                          <div class="card-body">
                            Le Président de la S.A.S.U.A.C.V. MERCORUS dirige la S.A.S.U.A.C.V.
                            MERCORUS et la représente à l'égard des tiers.
                            
                            <br>
                            <br>
                            
                            À ce titre, le Président de la S.A.S.U.A.C.V. MERCORUS est investi de tous les pouvoirs 
                            nécessaires pour agir en toutes circonstances au nom de la S.A.S.U.A.C.V. MERCORUS, dans la
                            limite de l'objet social et des domaines expressément réservés par la loi et les
                            présents statuts établis par l'actionnaire unique de la S.A.S.U.A.C.V.
                            MERCORUS.
                          </div>
                        </div>
                        <!-- Pouvoirs du Président -->
                        
                        <br>
                        <br>
                        
                        <!-- Pouvoirs du Président (en cas de Président-non associé unique de la S.A.S.U. à capital variable MERCORUS) -->
                        <div class="card text-center">
                          <div class="card-header">
                            Pouvoirs du Président (en cas de Président-non associé unique de la S.A.S.U. à capital variable MERCORUS)
                          </div>
                          <div class="card-body">
                            Toutefois, à titre de règlement intérieur non opposable aux tiers, le Président-non
                            associé unique de la S.A.S.U.A.C.V. MERCORUS ne peut prendre les décisions 
                            suivantes pour le compte de la S.A.S.U.A.C.V. MERCORUS qu'après avoir
                            obtenu l’autorisation préalable de l'associé unique de la S.A.S.U.A.C.V.
                            MERCORUS:
                            
                            <br>
                            
                            - Investissements supérieurs à cinq mille euros, ci 5 000,00 euros sous
                            n’importe quelle forme que ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Virements bancaires supérieurs à cinq mille euros, ci 5 000,00 euros sous
                            n’importe quelle forme que ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Opérations industrielles, mobilières et immobilières pouvant se rattacher
                            directement ou indirectement à l'objet social et à tous objets similaires ou
                            connexes pouvant favoriser son extension ou son développement sous
                            n’importe forme que ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Acceptation d’un contrat ou un traité ou un acte faisant intervenir en tant que
                            partie la S.A.S.U.A.C.V. MERCORUS sous n’importe quelle forme que ce
                            soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Acquisition ou cession d'un fonds de commerce ou d'éléments du fonds de
                            commerce de tous types que ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Acquisition ou cession de biens immobiliers de tous types que ce soit et pour
                            quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Prise ou mise en location-gérance de biens immobiliers de tous types que ce
                            soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Prise ou mise en location-gérance d'un fonds de commerce de tous types que
                            ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Acquisition ou cession de participations ou droits sociaux sous n’importe
                            quelle forme que ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Acquisition ou cession de droits de vote pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Acquisition ou cession ou location-gérance d’actions pour quelque motif que
                            ce soit ;
                            
                            <br>
                            <br>
                            
                            - Octroi de garanties sur l'actif social sous n’importe quelle forme que ce soit et
                            pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Octroi de crédit ou prêt sous n’importe quelle forme que ce soit et pour
                            quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Demande de crédit ou prêt sous n’importe quelle forme que ce soit et pour
                            quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Création de filiales et prise de participations sous n’importe quelle forme que
                            ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Rachat de crédit ou prêt sous n’importe quelle forme que ce soit et pour
                            quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Opération financière sous n'importe quelle forme que ce soit et pour quelque
                            motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Abandon de créances sous n’importe quelle forme que ce soit et pour
                            quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Achat de tampons encreurs sous n’importe forme que ce soit et pour quelque
                            motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Ouverture d’un compte bancaire sous n’importe quelle forme que ce soit et
                            pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Choix d’un comptable ou expert-comptable sous n’importe quelle forme que
                            ce soit et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Choix d’un commissaire aux comptes sous n’importe quelle forme que ce soit
                            et pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Choix d’un logiciel de paie sous n’importe quelle forme que ce soit et pour
                            quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Choix d’un logiciel de comptabilité sous n’importe quelle forme que ce soit et
                            pour quelque motif que ce soit ;
                            
                            <br>
                            <br>
                            
                            - Conservation des documents à son domicile sous n’importe quelle forme que
                            ce soit et pour quelque motif que ce soit.
                            
                            <br>
                            <br>
                            
                            Le Président-non associé unique de la S.A.S.U.A.C.V. MERCORUS peut, sous
                            sa pleine et entière responsabilité, consentir toutes délégations de pouvoirs à tout
                            tiers pour un ou plusieurs objets déterminés.
                            
                            <br>
                            <br>
                            
                            La S.A.S.U.A.C.V. MERCORUS est engagée à l'égard des tiers même par les
                            actes du Président-non associé unique de la S.A.S.U.A.C.V. MERCORUS qui ne
                            relèvent pas de l'objet social, sauf si elle apporte la preuve que le tiers avait
                            connaissance du dépassement de l'objet social de la S.A.S.U.A.C.V.
                            MERCORUS ou qu'il ne pouvait l'ignorer compte tenu des circonstances, la
                            publication des statuts ne pouvant, à elle seule, suffire à constituer cette preuve.
                          </div>
                        </div>
                        <!-- Pouvoirs du Président (en cas de Président-non associé unique de la S.A.S.U. à capital variable MERCORUS) -->
                      </div>
                    </div>
                    <!-- Article 13 - Président de la S.A.S.U. à capital variable MERCORUS -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 14 - Conventions entre la S.A.S.U. à capital variable MERCORUS et ses dirigeants -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 14 - Conventions entre la S.A.S.U. à capital variable MERCORUS et ses dirigeants
                      </div>
                      <div class="card-body">
                        Le commissaire aux comptes établit un rapport sur les conventions conclues
                        directement ou par personne interposée entre la S.A.S.U.A.C.V. MERCORUS et
                        son Président, ou ses autres dirigeants, ou de l’actionnaire unique de la
                        S.A.S.U.A.C.V. MERCORUS des droits de vote, au cours de l'exercice écoulé.
                        
                        <br>
                        <br>
                        
                        La collectivité des associés de la S.A.S.U.A.C.V. MERCORUS statue chaque année
                        sur ce rapport lors de sa consultation annuelle sur les comptes sociaux de la
                        S.A.S.U.A.C.V. MERCORUS dudit exercice écoulé.
                        
                        <br>
                        <br>
                        
                        Toute convention intervenant directement ou par personne interposée entre la
                        S.A.S.U.A.C.V. MERCORUS et le Président-associé unique de la S.A.S.U.A.C.V.
                        MERCORUS est mentionnée au registre des décisions de l'associé unique de la
                        S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        Toutes conventions, autres que celles portant sur des opérations courantes conclues
                        à des conditions normales, entre la S.A.S.U.A.C.V. MERCORUS et son Président
                        et ses autres dirigeants ou son actionnaire unique, intervenues directement ou par
                        personne interposée, doivent être portées à la connaissance du commissaire aux
                        comptes dans le délai d'un mois du jour de sa conclusion.
                        
                        <br>
                        <br>
                        
                        Les conventions non approuvées par un commissaire aux comptes produisent
                        néanmoins leurs effets, à charge pour la personne intéressée et, éventuellement,
                        pour le Président et les autres dirigeants de la S.A.S.U.A.C.V. MERCORUS d'en
                        supporter les conséquences dommageables pour la S.A.S.U.A.C.V.
                        MERCORUS.
                      </div>
                    </div>
                    <!-- Article 14 - Conventions entre la S.A.S.U. à capital variable MERCORUS et ses dirigeants -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 15 - Commissaires aux comptes -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 15 - Commissaires aux comptes
                      </div>
                      <div class="card-body">
                        Vu l’article L227-9-1 du code de commerce,
                        
                        <br>
                        <br>
                        
                        Vu les articles L823-1 à L823-8-1 du code de commerce,
                        
                        <br>
                        <br>
                        
                        Vu l’article R823-7 du code de commerce,
                        
                        <br>
                        <br>
                        
                        Vu l’article R823-7-1 du code de commerce,
                        
                        <br>
                        <br>
                        
                        Vu le décret n° 2019-514 du 24 mai 2019 fixant les seuils de désignation des
                        commissaires aux comptes et les délais pour élaborer les normes d'exercice
                        professionnel,
                        
                        <br>
                        <br>
                        
                        Un ou plusieurs commissaire(s) aux comptes titulaire(s) et un ou plusieurs
                        commissaire(s) aux comptes suppléant(s) doivent être désignés par décision de
                        l’associé unique de la S.A.S.U.A.C.V. MERCORUS, dans les conditions et aux
                        fins d'accomplir les missions définies par la loi, notamment celle de contrôler les
                        comptes sociaux de la S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        La désignation d'un commissaire aux comptes n'est obligatoire que si la condition
                        suivante est remplie :
                        
                        <br>
                        
                        - la S.A.S.U.A.C.V. MERCORUS dépasse à la clôture de l'exercice deux des
                        seuils suivants : total du bilan supérieur à quatre millions d'euros, chiffre d'affaires
                        hors taxes supérieur à huit millions d'euros, et/ou nombre moyen de salariés
                        permanents employés au cours de l'exercice dépassant cinquante salariés.
                      </div>
                    </div>
                    <!-- Article 15 - Commissaires aux comptes -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 16 – Comité social et économique -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 16 – Comité social et économique
                      </div>
                      <div class="card-body">
                        Vu les articles L2311-1 à L2317-2 du code du travail,
                        
                        <br>
                        <br>
                        
                        Un comité social et économique est mis en place si la S.A.S.U.A.C.V.
                        MERCORUS atteint au moins onze salariés.
                        
                        <br>
                        <br>
                        
                        Sa mise en place n'est obligatoire que si l'effectif d'au moins onze salariés est atteint
                        pendant douze mois consécutifs au sein de la S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        Les articles L2311-1 à L2317-2 du code du travail devront être mis en application
                        afin de garantir :
                        
                        <br>
                        
                        - Les attributions du comité social et économique ;
                        
                        <br>
                        <br>
                        
                        - La mise en place et suppression du comité social et économique ;
                        
                        <br>
                        <br>
                        
                        - La composition, les élections et le mandat des membres de la délégation du
                        personnel du comité social et économique ;
                        
                        <br>
                        <br>
                        
                        - Le fonctionnement du comité social et économique ;
                        
                        <br>
                        <br>
                        
                        - La mise en application du comité social et économique central et comité
                        social et économique d'établissement.
                      </div>
                    </div>
                    <!-- Article 16 – Comité social et économique -->
                  </div>
                </div>
                <!-- TITRE III - ADMINISTRATION ET DIRECTION DE LA SOCIETE / CONVENTIONS ENTRE LA SOCIETE ET SON 
                    DIRIGEANT / COMMISSAIRES AUX COMPTES -->
                
                <br>
                <br>
                
                <!-- TITRE IV - DECISIONS DE L'ACTIONNAIRE UNIQUE -->
                <div class="card text-center">
                  <div class="card-header">
                    TITRE IV - DECISIONS DE L'ACTIONNAIRE UNIQUE
                  </div>
                  <div class="card-body">
                    <!-- Article 17 - Décisions de l'associé unique de la S.A.S.U.A.C.V. MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 17 - Décisions de l'associé unique de la S.A.S.U.A.C.V. MERCORUS
                      </div>
                      <div class="card-body">
                        <!-- Domaine réservé à l'associé unique de la S.A.S.U.A.C.V. MERCORUS -->
                        <div class="card text-center">
                          <div class="card-header">
                            Domaine réservé à l'associé unique de la S.A.S.U.A.C.V. MERCORUS
                          </div>
                          <div class="card-body">
                            L'associé unique de la S.A.S.U.A.C.V. MERCORUS est seul compétent pour
                            prendre les décisions suivantes pour le compte de la S.A.S.U.A.C.V. MERCORUS :
                            
                            <br>
                            
                            - L’approbation des comptes sociaux de la S.A.S.U.A.C.V. MERCORUS et
                            l’affectation et répartition du résultat de la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La nomination et la révocation du Président de la S.A.S.U.A.C.V.
                            MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - L'agrément d'un nouvel associé à la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - L'approbation du rapport spécial du Président de la S.A.S.U.A.C.V.
                            MERCORUS sur les conventions réglementées de la S.A.S.U.A.C.V.
                            MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La création de filiales et la prise de participations pour le compte de la
                            S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La rémunération du Président de la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La nomination des commissaires aux comptes pour le compte de la
                            S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La nomination des liquidateurs pour le compte de la S.A.S.U.A.C.V.
                            MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La transformation, la fusion, la scission et l’apport partiel d’actif de la
                            S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - L’augmentation, la réduction ou l’amortissement du capital social de la
                            S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - Les autres modifications des statuts de la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - Le transfert du siège social de la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - Le changement de dénomination sociale de la S.A.S.U.A.C.V.
                            MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - Le changement et/ou la souscription de compte bancaire pour le compte de la
                            S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - L’annulation de toutes décisions prises par le président de la S.A.S.U.A.C.V.
                            MERCORUS, les employés et les tiers de la S.A.S.U.A.C.V.
                            MERCORUS pour le compte de la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La cession de droits sociaux de la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La dissolution et la liquidation de la S.A.S.U.A.C.V. MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - L’achat de tampons encreurs pour le compte de la S.A.S.U.A.C.V.
                            MERCORUS ;
                            
                            <br>
                            <br>
                            
                            - La mise en place de dépenses de recherches et développement.
                            
                            <br>
                            <br>
                            
                            En cas de limitation des pouvoirs du Président-non associé unique de la
                            S.A.S.U.A.C.V. MERCORUS, l’autorisation des décisions du Président-non
                            associé unique de la S.A.S.U.A.C.V. MERCORUS sont visées à l'article 13 des
                            présents statuts.
                            
                            <br>
                            <br>
                            
                            L'associé unique de la S.A.S.U.A.C.V. MERCORUS ne peut pas déléguer ses
                            pouvoirs.
                            
                            <br>
                            <br>
                            
                            Toutes les autres décisions sont de la compétence du Président-non associé unique
                            de la S.A.S.U.A.C.V. MERCORUS.
                          </div>
                        </div>
                        <!-- Domaine réservé à l'associé unique de la S.A.S.U.A.C.V. MERCORUS -->
                        
                        <br>
                        <br>
                        
                        <!-- Forme des décisions -->
                        <div class="card text-center">
                          <div class="card-header">
                            Forme des décisions
                          </div>
                          <div class="card-body">
                            Les décisions de l'actionnaire unique de la S.A.S.U.A.C.V. MERCORUS sont répertoriées dans 
                            un registre coté et paraphé tenu par la S.A.S.U.A.C.V. MERCORUS à l’adresse du siège 
                            social de la S.A.S.U.A.C.V. MERCORUS ou au domicile de l'actionnaire unique de la 
                            S.A.S.U.A.C.V. MERCORUS.
                          </div>
                        </div>
                        <!-- Forme des décisions -->
                      </div>
                    </div>
                    <!-- Article 17 - Décisions de l'associé unique de la S.A.S.U.A.C.V. MERCORUS -->
                  </div>
                </div>
                <!-- TITRE IV - DECISIONS DE L'ACTIONNAIRE UNIQUE -->
                
                <br>
                <br>
                
                <!-- TITRE V - EXERCICE SOCIAL / COMPTES SOCIAUX / AFFECTATION DES RESULTATS -->
                <div class="card text-center">
                  <div class="card-header">
                    TITRE V - EXERCICE SOCIAL / COMPTES SOCIAUX / AFFECTATION DES RESULTATS
                  </div>
                  <div class="card-body">
                    <!-- Article 18 - Exercice social -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 18 - Exercice social
                      </div>
                      <div class="card-body">
                        L'exercice social de la S.A.S.U.A.C.V. MERCORUS commence au premier jour
                        du mois de janvier et se termine au dernier jour du mois de décembre de chaque
                        année.
                        
                        <br>
                        <br>
                        
                        Exceptionnellement, le premier exercice social de la S.A.S.U.A.C.V. MERCORUS
                        commencera à courir à compter de la date de l'immatriculation de la S.A.S.U.A.C.V.
                        MERCORUS au Registre du Commerce et des Sociétés et sera clos le dernier
                        jour du mois de décembre de l’année identique à l’année de la date de
                        l’immatriculation de la S.A.S.U.A.C.V. MERCORUS au Registre du Commerce et
                        des Sociétés.
                      </div>
                    </div>
                    <!-- Article 18 - Exercice social -->
                    
                    <br>
                    <br>
                            
                    <!-- Article 19 - Comptes sociaux -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 19 - Comptes sociaux
                      </div>
                      <div class="card-body">
                        Vu l’article L227-9 du code de commerce,
                        
                        <br>
                        <br>
                            
                        Vu les articles L232-1 à L232-26 du code de commerce concernant les comptes
                        sociaux,
                        
                        <br>
                        <br>
                        
                        Vu les articles R123-111 à R123-111-1 du code de commerce concernant le dépôt
                        des documents comptables et de la déclaration de confidentialité des comptes
                        annuels,
                        
                        <br>
                        <br>
                        
                        Vu les articles R232-1 à R232-22 du code de commerce concernant les comptes
                        sociaux,
                        
                        <br>
                        <br>
                        
                        Vu les articles A123-61 à A123-62 du Code de commerce concernant le dépôt des
                        documents comptables et de la déclaration de confidentialité des comptes annuels,
                        
                        <br>
                        <br>
                        
                        <!-- Établissement des comptes sociaux de la S.A.S.U.A.C.V. MERCORUS -->
                        <div class="card text-center">
                          <div class="card-header">
                            Établissement des comptes sociaux de la S.A.S.U.A.C.V. MERCORUS
                          </div>
                          <div class="card-body">
                            Il est tenu une comptabilité régulière des opérations sociales, conformément à la loi
                            et aux usages du commerce.
                            
                            <br>
                            <br>
                            
                            À la clôture de chaque exercice social de la S.A.S.U.A.C.V. MERCORUS, le
                            Président de la S.A.S.U.A.C.V. MERCORUS dresse le livre d'inventaire des
                            divers éléments de l'actif et du passif existant à cette date.
                            
                            <br>
                            <br>
                            
                            Le Président de la S.A.S.U.A.C.V. MERCORUS dresse également le bilan
                            décrivant les éléments actifs et passifs et faisant apparaître de façon distincte les
                            capitaux propres, le compte de résultat récapitulant les produits et les charges de
                            l’exercice social, ainsi que l’annexe complétant et commentant l’information donnée
                            par le bilan et le compte de résultat.
                            
                            <br>
                            <br>
                            
                            Le Président de la S.A.S.U.A.C.V. MERCORUS établit le rapport de gestion sur
                            la situation de la S.A.S.U.A.C.V. MERCORUS durant l'exercice social écoulé, son
                            évolution prévisible, les événements importants survenus entre la date de clôture de
                            l’exercice social et la date à laquelle il est établi, ses activités en matière de
                            recherche et de développement.
                            
                            <br>
                            <br>
                            
                            Tous ces documents sont mis à la disposition du commissaire aux comptes de la
                            S.A.S.U.A.C.V. MERCORUS dans les conditions légales, le cas échéant.
                            
                            <br>
                            <br>
                            
                            L'associé unique de la S.A.S.U.A.C.V. MERCORUS doit approuver les comptes
                            sociaux de la S.A.S.U.A.C.V. MERCORUS de l’exercice social écoulé de la
                            S.A.S.U.A.C.V. MERCORUS après rapport général du commissaire aux
                            comptes, le cas échéant, dans un délai de six mois à compter de la clôture de
                            chaque exercice.
                          </div>
                        </div>
                        <!-- Établissement des comptes sociaux de la S.A.S.U.A.C.V. MERCORUS -->
                        
                        <br>
                        <br>
                        
                        <!-- Dépôt des comptes sociaux de la S.A.S.U.A.C.V. MERCORUS -->
                        <div class="card text-center">
                          <div class="card-header">
                            Dépôt des comptes sociaux de la S.A.S.U.A.C.V. MERCORUS
                          </div>
                          <div class="card-body">
                            La S.A.S.U.A.C.V. MERCORUS est tenue de déposer au greffe du tribunal de
                            commerce, pour être annexés au Registre du Commerce et des Sociétés, dans le
                            mois suivant l'approbation des comptes annuels de la S.A.S.U.A.C.V.
                            MERCORUS par l’associé unique de la S.A.S.U.A.C.V. MERCORUS ou dans
                            les deux mois suivant cette approbation lorsque ce dépôt est effectué par voie
                            électronique :
                            
                            <br>
                            
                            - Les comptes annuels, le rapport de gestion, le rapport du (ou des)
                            commissaire(s) aux comptes sur les comptes annuels, le cas échéant,
                            éventuellement complété de leurs observations sur les modifications
                            apportées par l'assemblée des associés de la S.A.S.U.A.C.V.
                            MERCORUS aux comptes annuels de la S.A.S.U.A.C.V. MERCORUS
                            qui ont été soumis à cette dernière ainsi que, le cas échéant, les comptes
                            consolidés, le rapport sur la gestion du groupe, le rapport du (ou des)
                            commissaire(s) aux comptes sur les comptes consolidés et le rapport du
                            conseil de surveillance ;
                            
                            <br>
                            <br>
                                
                            - La proposition d'affectation du résultat soumise à l'actionnaire unique de la
                            S.A.S.U.A.C.V. MERCORUS.
                            
                            <br>
                            <br>
                            
                            La S.A.S.U.A.C.V. MERCORUS est tenue de joindre une déclaration de
                            confidentialité des comptes annuels lors du dépôt des documents comptables
                            auprès du greffe du tribunal de commerce, le cas échéant.
                          </div>
                        </div>
                        <!-- Dépôt des comptes sociaux de la S.A.S.U.A.C.V. MERCORUS -->
                      </div>
                    </div>
                    <!-- Article 19 - Comptes sociaux -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 20 - Affectation et répartition du résultat -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 20 - Affectation et répartition du résultat
                      </div>
                      <div class="card-body">
                        Vu les articles L232-10 à L232-20 du code de commerce,
                        
                        <br>
                        <br>
                            
                        Vu les articles R232-17 à R232-18 du code de commerce,
                        
                        <br>
                        <br>
                        
                        <!-- Bénéfice -->
                        <div class="card text-center">
                          <div class="card-header">
                            Bénéfice
                          </div>
                          <div class="card-body">
                            Le compte de résultat récapitule les produits et les charges de l'exercice.
                            
                            <br>
                            <br>
                                
                            Il fait apparaître, par différence, après déduction des amortissements et des
                            provisions, le bénéfice ou la perte de l'exercice.
                            
                            <br>
                            <br>
                            
                            Sur ce bénéfice, diminué, le cas échéant, des pertes antérieures, il est d'abord
                            prélevé :
                            
                            <br>
                            
                            a) Un vingtième (5 %) au moins affecté à la formation d'un fonds de réserve dit
                            "réserve légale".
                            
                            <br>
                            
                            En vertu de l’article L232-10 du code de commerce, ce prélèvement cessera d'être
                            obligatoire lorsque le fonds de réserve légale aura atteint le dixième du capital social
                            de la S.A.S.U.A.C.V. MERCORUS, mais reprendra son cours si, pour une cause
                            quelconque, cette quotité n'est plus atteinte ;
                            
                            <br>
                            <br>
                            
                            b) Toutes sommes à porter sous réserve de l’application de la loi et des présents
                            statuts.
                            
                            <br>
                            
                            En vertu de l’article L232-11 du code de commerce, le bénéfice distribuable est
                            constitué par le bénéfice de l'exercice, diminué des pertes antérieures, ainsi que des
                            sommes à porter en réserve en application de la loi ou des statuts, et augmenté du
                            report bénéficiaire.
                          </div>
                        </div>
                        <!-- Bénéfice -->
                        
                        <br>
                        <br>
                        
                        <!-- Bénéfice distribuable -->
                        <div class="card text-center">
                          <div class="card-header">
                            Bénéfice distribuable
                          </div>
                          <div class="card-body">
                            Sur le bénéfice distribuable de la S.A.S.U.A.C.V. MERCORUS, il est prélevé tout
                            d'abord toute somme que l'actionnaire unique de la S.A.S.U.A.C.V. MERCORUS
                            décidera de reporter à nouveau sur l'exercice suivant ou d'affecter à la création de
                            tous fonds de réserve extraordinaire, de prévoyance ou autre avec une affectation
                            spéciale ou non.
                            
                            <br>
                            <br>
                            
                            Le surplus est attribué à l'actionnaire unique de la S.A.S.U.A.C.V.
                            MERCORUS.
                            
                            <br>
                            <br>
                            
                            En vertu de l’article L232-13 du code de commerce, la mise en paiement des
                            dividendes doit avoir lieu dans un délai maximal de neuf mois après la clôture de
                            l'exercice social de la S.A.S.U.A.C.V. MERCORUS. 
                            
                            <br>
                            <br>
                            
                            La prolongation de ce délai peut être accordée par décision de justice.
                            
                            <br>
                            <br>
                            
                            L'actionnaire unique de la S.A.S.U.A.C.V. MERCORUS peut décider d'opter, pour
                            tout ou partie du dividende mis en distribution, entre le paiement du dividende en
                            numéraire ou en actions émises par la S.A.S.U.A.C.V. MERCORUS, ceci aux
                            conditions fixées ou autorisées par la loi.
                          </div>
                        </div>
                        <!-- Bénéfice distribuable -->
                      </div>
                    </div>
                    <!-- Article 20 - Affectation et répartition du résultat -->
                  </div>
                </div>
                <!-- TITRE V - EXERCICE SOCIAL / COMPTES SOCIAUX / AFFECTATION DES RESULTATS -->
                
                <br>
                <br>
                
                <!-- TITRE VI - DISSOLUTION DE LA SOCIETE -->
                <div class="card text-center">
                  <div class="card-header">
                    TITRE VI - DISSOLUTION DE LA SOCIETE
                  </div>
                  <div class="card-body">
                    <!-- Article 21 - Dissolution de la S.A.S.U. à capital variable MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 21 - Dissolution de la S.A.S.U. à capital variable MERCORUS
                      </div>
                      <div class="card-body">
                        Vu les articles L237-1 à L237-13 du code de commerce concernant la liquidation,
                        
                        <br>
                        <br>
                        
                        Vu les articles R237-1 à R237-9 du code de commerce concernant la liquidation,
                        
                        <br>
                        <br>
                        
                        La S.A.S.U.A.C.V. MERCORUS est dissoute dans les cas prévus par la loi ou en
                        cas de dissolution anticipée décidée par l'associé unique de la S.A.S.U.A.C.V.
                        MERCORUS.
                        
                        <br>
                        <br>
                        
                        Lorsque l'associé unique de la S.A.S.U.A.C.V. MERCORUS est une personne
                        morale, la dissolution de la S.A.S.U.A.C.V. MERCORUS entraîne, dans les
                        conditions prévues à l'article 1844-5 du Code civil, la transmission universelle du
                        patrimoine de la S.A.S.U.A.C.V. MERCORUS à l'associé unique de la
                        S.A.S.U.A.C.V. MERCORUS, sans qu'il y ait lieu à liquidation.
                        
                        <br>
                        <br>
                        
                        Lorsque l'associé unique de la S.A.S.U.A.C.V. MERCORUS est une personne
                        physique, la dissolution de la S.A.S.U. à capital variable MERCORUS entraîne sa
                        liquidation.
                        
                        <br>
                        <br>
                        
                        L'associé unique de la S.A.S.U.A.C.V. MERCORUS nomme un ou plusieurs
                        liquidateur(s).
                        
                        <br>
                        <br>
                        
                        Le (ou les) liquidateur(s) sont investis des pouvoirs les plus étendus, sous réserve
                        des dispositions légales, pour réaliser l'actif, payer le passif et distribuer le solde
                        disponible à l'associé unique de la S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        En fin de liquidation, l'associé unique de la S.A.S.U.A.C.V. MERCORUS statue
                        sur les comptes définitifs, sur le quitus de la gestion du (ou des) liquidateurs et la (ou
                        les) décharge(s) de son (ou de leur) mandat et constate la clôture de la liquidation.
                      </div>
                    </div>
                    <!-- Article 21 - Dissolution de la S.A.S.U. à capital variable MERCORUS -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 22 – Contestations -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 22 – Contestations
                      </div>
                      <div class="card-body">
                        Vu les articles L721-1 à L721-2 du code de commerce concernant l'institution et la
                        compétence du tribunal de commerce,
                        
                        <br>
                        <br>
                            
                        Vu les articles L721-3 à L721-7 du code de commerce concernant la compétence
                        commune à tous les tribunaux de commerce,
                        
                        <br>
                        <br>
                        
                        Vu l’article L721-8 du code de commerce concernant la compétence particulière à
                        certains tribunaux de commerce,
                        
                        <br>
                        <br>
                        
                        Vu les articles R621-1 à R621-16 du code de commerce concernant la saisine et la
                        décision du tribunal de l'ouverture de la procédure de la sauvegarde,
                        
                        <br>
                        <br>
                        
                        Vu les articles R631-1 à R631-15 du code de commerce concernant la saisine et la
                        décision du tribunal pour l'ouverture de la procédure du redressement judiciaire,
                        
                        <br>
                        <br>
                        
                        Vu les articles R640-1 à R640-2 du code de commerce concernant l'ouverture et du
                        déroulement de la liquidation judiciaire,
                        
                        <br>
                        <br>
                        
                        Vu les articles R641-1 à R641-9 du code de commerce concernant la saisine et la
                        décision du tribunal du jugement de liquidation judiciaire,
                        
                        <br>
                        <br>
                        
                        Vu les articles R721-1 à R721-4 du code de commerce concernant les dispositions
                        générales du tribunal de commerce,
                        
                        <br>
                        <br>
                        
                        Vu les articles R721-5 à R721-6 du code de commerce concernant la compétence
                        du tribunal de commerce,
                        
                        <br>
                        <br>
                        
                        Toutes contestations relatives aux affaires sociales qui pourront surgir pendant la
                        durée de la S.A.S.U.A.C.V. MERCORUS ou de sa liquidation seront soumises
                        aux tribunaux compétents dans les conditions de droit commun et des compétences
                        particulières.
                      </div>
                    </div>
                    <!-- Article 22 – Contestations -->
                  </div>
                </div>
                <!-- TITRE VI - DISSOLUTION DE LA SOCIETE -->
                                
                <br>
                <br>
                
                <!-- TITRE VII - CONSTITUTION DE LA S.A.S.U. À CAPITAL VARIABLE MERCORUS -->
                <div class="card text-center">
                  <div class="card-header">
                    TITRE VII - CONSTITUTION DE LA S.A.S.U. À CAPITAL VARIABLE MERCORUS
                  </div>
                  <div class="card-body">
                    <!-- Article 23 - Nomination du Président de la S.A.S.U. à capital variable MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 23 - Nomination du Président de la S.A.S.U. à capital variable MERCORUS
                      </div>
                      <div class="card-body">
                        Vu l’article L227-6 du Code de commerce,
                        
                        <br>
                        <br>
                        
                        Monsieur , né le  à
                        Saint-Louis (97450) de nationalité française, demeurant au 
                        Étage 1 – Porte 6 93800 Épinay-sur-Seine, Président-associé unique de la
                        S.A.S.U.A.C.V. MERCORUS, exerce la présidence de la S.A.S.U.A.C.V.
                        MERCORUS aux termes des présents statuts sans limitation de durée.
                      </div>
                    </div>
                    <!-- Article 23 - Nomination du Président de la S.A.S.U. à capital variable MERCORUS -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 24 - Actes accomplis pour le compte de la S.A.S.U. à capital variable MERCORUS en formation -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 24 - Actes accomplis pour le compte de la S.A.S.U. à capital variable MERCORUS en formation
                      </div>
                      <div class="card-body">
                        Monsieur  né le  à SaintLouis (97450) de 
                        nationalité française, demeurant au  Étage 1 Porte 6 93800 
                        Épinay-sur-Seine, Président-associé unique de la S.A.S.U.A.C.V. MERCORUS en formation, 
                        a établi un état des actes accomplis à ce jour pour le
                        compte de la S.A.S.U.A.C.V. MERCORUS en formation avec l'indication pour
                        chacun d'eux, des engagements qui en résulteraient pour la S.A.S.U.A.C.V.
                        MERCORUS.
                        
                        <br>
                        <br>
                        
                        Cet état est annexé aux présents statuts.
                        
                        <br>
                        <br>
                        
                        L'immatriculation de la S.A.S.U.A.C.V. MERCORUS au Registre du Commerce et
                        des Sociétés entraînera de plein droit reprise par la S.A.S.U.A.C.V. MERCORUS
                        desdits actes et engagements.
                      </div>
                    </div>
                    <!-- Article 24 - Actes accomplis pour le compte de la S.A.S.U. à capital variable MERCORUS en formation -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 25 – Mandat de prendre des engagements pour le compte de la S.A.S.U. à capital variable MERCORUS -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 25 – Mandat de prendre des engagements pour le compte de la S.A.S.U. à capital variable MERCORUS
                      </div>
                      <div class="card-body">
                        Vu l’article 1843 du code civil,
                        
                        <br>
                        <br>
                            
                        Vu l’article L210-6 du code de commerce,
                        
                        <br>
                        <br>
                        
                        Vu l’article R210-6 du code de commerce,
                        
                        <br>
                        <br>
                        
                        Monsieur , né le  à
                        Saint-Louis (97450) de nationalité française, demeurant au 
                        Étage 1 Porte 6 93800 Épinay-sur-Seine, Président-associé unique de la
                        S.A.S.U.A.C.V. MERCORUS, agira au nom et pour le compte de la
                        S.A.S.U.A.C.V. MERCORUS en formation, jusqu'à son immatriculation au
                        Registre du Commerce et des Sociétés.
                        
                        <br>
                        <br>
                        
                        Il passera les actes et prendra les engagements au nom et pour le compte de la 
                        S.A.S.U.A.C.V. MERCORUS.
                        
                        <br>
                        <br>
                        
                        L'immatriculation de la S.A.S.U.A.C.V. MERCORUS au Registre du Commerce et
                        des Sociétés emportera reprise de ces actes et engagements.
                      </div>
                    </div>
                    <!-- Article 25 – Mandat de prendre des engagements pour le compte de la S.A.S.U. à capital variable MERCORUS -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 26 - Formalités de publicité – Immatriculation -->
                    <div class="card text-center">
                      <div class="card-header">
                        Article 26 - Formalités de publicité – Immatriculation
                      </div>
                      <div class="card-body">
                        Vu les articles L123-1 à L123-5-2 du code de commerce concernant les personnes
                        tenues à l'immatriculation,
                        
                        <br>
                        <br>
                            
                        Vu les articles L123-6 à L123-9-1 du code de commerce concernant la tenue du
                        registre et effets attachés à l'immatriculation,
                        
                        <br>
                        <br>
                        
                        Vu l’article R123-31 du code de commerce concernant l'obligation d'immatriculation,
                        
                        <br>
                        <br>
                        
                        Vu les articles R123-35 à R123-36 du code de commerce concernant l'obligation
                        d'immatriculation des personnes morales,
                        
                        <br>
                        <br>
                        
                        Vu les articles R123-53 à R123-62 du code de commerce concernant les
                        déclarations incombant aux personnes morales aux fins d'immatriculation,
                        
                        <br>
                        <br>
                        
                        Vu les articles R210-16 à R210-20 du code de commerce concernant les formalités
                        de publicité,
                        
                        <br>
                        <br>
                        
                        Vu les articles R123-155 à R123-162 du code de commerce concernant la
                        publication au Bulletin officiel des annonces civiles et commerciales,
                        
                        <br>
                        <br>
                        
                        Tous pouvoirs sont conférés au Président-associé unique de la S.A.S.U.A.C.V.
                        MERCORUS à l'effet de signer l'insertion relative à la constitution de la
                        S.A.S.U.A.C.V. MERCORUS dans un journal d'annonces légales et au porteur
                        d'un original, d'une copie ou d'un extrait des présents statuts de la S.A.S.U.A.C.V.
                        MERCORUS pour accomplir toutes autres formalités nécessaires pour parvenir à
                        l'immatriculation de la S.A.S.U.A.C.V. MERCORUS au Registre du Commerce et
                        des Sociétés.
                      </div>
                    </div>
                    <!-- Article 26 - Formalités de publicité – Immatriculation -->
                  </div>
                </div>
                <!-- TITRE VII - CONSTITUTION DE LA S.A.S.U. À CAPITAL VARIABLE MERCORUS -->
                
                <br>
                <br>
                
                <!-- Acceptation des statuts de la société MERCORUS -->
                <div class="card text-center">
                  <div class="card-header">
                    Acceptation des statuts de la société MERCORUS
                  </div>
                  <div class="card-body">
                    Fait à Epinay-sur-Seine (93800), le 20 Mars 2021.
                    
                    <br>
                    <br>
                    
                    En 6 exemplaires originaux pour le dépôt d'un exemplaire original au domicile du
                    Président-associé unique de la S.A.S.U.A.C.V. MERCORUS et l'exécution des
                    diverses formalités légales pour le compte de la S.A.S.U.A.C.V. MERCORUS.
                    
                    <br>
                    <br>
                    
                    Bon pour acceptation des fonctions de Président-associé unique de la
                    S.A.S.U.A.C.V. MERCORUS par Monsieur Jason Aymérick Jean Claudius
                    ALOYAU.
                    
                    <br>
                    <br>
                    
                    Visé par Monsieur , Président-associé
                    unique de la S.A.S.U.A.C.V. MERCORUS.
                    
                    <br>
                    <br>
                    
                    Apposition de la signature de l'actionnaire unique de la S.A.S.U.A.C.V. MERCORUS précédée 
                    de la mention «Lu et approuvé» en bas de page de la dernière page des statuts de la 
                    société MERCORUS.
                  </div>
                </div>
                <!-- Acceptation des statuts de la société MERCORUS -->
                
                <br>
                <br>
                
              </div>
            </div>
            
            <br>
            <br>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'header-center': 'Les statuts de la société MERCORUS',
            'footer-left': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        pdfkit.from_string(body,
                           "Mercorus\\Statuts_De_La_Societe_Mercorus.pdf",
                           configuration=config,
                           options=options)

        filename = "Mercorus\\Statuts_De_La_Societe_Mercorus.pdf"

        date_of_today = dt.today().strftime('%d_%m_%Y')

        filename_to_sign = filename.split(".pdf")[0] + "_" + date_of_today + ".pdf"

        try:
            packet = io.BytesIO()

            # create a new PDF with Reportlab
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFontSize(8)

            x_coord = 5.9 * 72

            y_coord = 0.14 * 72

            date_of_signature = dt.today().strftime('%d/%m/%Y')

            # Insérer la valeur "Fait à Epinay-sur-Seine (), le dd/mm/YYYY.".
            can.drawString(x_coord, y_coord, "Fait à Epinay-sur-Seine (93800), le " + date_of_signature + ".")

            # Insérer la valeur "Lu et approuvé.".
            can.drawString(x_coord, y_coord - 8, "Lu et approuvé.")

            can.save()

            # move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PdfFileReader(packet)

            # read your existing PDF
            existing_pdf = PdfFileReader(open(filename, "rb"))

            page_number = existing_pdf.getNumPages()

            output = PdfFileWriter()

            # add the "text" (which is the new pdf) on the existing page
            last_page = existing_pdf.getPage(page_number - 1)
            last_page.mergePage(new_pdf.getPage(0))

            # add every pages of existing_pdf except the last page to output
            for i in range(0, page_number - 1):
                output.addPage(existing_pdf.getPage(i))

            output.addPage(last_page)

            # finally, write "output" to a real file
            output_stream = open(filename_to_sign, "wb")
            output.write(output_stream)
            output_stream.close()

            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(filename_to_sign, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = 4.4 * 72

            y_coord = 0.03 * 72

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(filename_to_sign) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(round(x_coord)) + "x" + str(round(y_coord)) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))

    # ok
    # https://www.cagi.ch/fr/infos-pratiques/modele-statuts-association/
    def test_statuts_association_mytrapcoo(self):
        print("test_statuts_association_mytrapcoo")

        body = """
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" 
            integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">

            <title>Les statuts de l'association à buts de service public MyTrapCoo</title>
          </head>
          <body>
            <div class="card text-center">
              <div class="card-header">
                Les statuts de l'association à buts de service public MyTrapCoo
              </div>
              <div class="card-body">
                <!-- Informations générales de l'association à buts de service public MyTrapCoo -->
                <div class="card text-center">
                  <div class="card-header">
                    Informations générales de l'association à buts de service public MyTrapCoo
                  </div>
                  <div class="card-body">
                    MyTrapCoo, association à buts de service public
                    <br>
                    Siège social : Canton de Genève
                    <br>
                    Président de l'assemblée constitutive : Monsieur 
                  </div>
                </div>
                <!-- Informations générales de l'association à buts de service public MyTrapCoo -->

                <br>
                <br>

                <!-- Responsable de la rédaction -->
                <div class="card text-center">
                  <div class="card-header">
                    Responsable de la rédaction des statuts de l'association à buts de service public MyTrapCoo
                  </div>
                  <div class="card-body">
                    Je soussigné Monsieur  né le  à 
                    Saint-Louis (97450) ayant pour adresse postale de correspondance au .... 
                    de nationalité française a établi ainsi qu'il suit les statuts de l'association à buts de service 
                    public MyTrapCoo qu'il a décidé d'instituer.
                  </div>
                </div>
                <!-- Responsable de la rédaction -->

                <br>
                <br>
                
                <!-- Préambule  -->
                <div class="card text-center">
                  <div class="card-header">
                    Préambule 
                  </div>
                  <div class="card-body">
                    Dans un temps d'urgence écologique mondiale, l'origine de l'Association MyTrapCoo est venue à 
                    l'idée de son Fondateur, Monsieur , pour parvenir à résoudre 
                    un problème global lié à la protection de l'environnement dont "le réchauffement climatique".
                    
                    <br>
                    <br>
                    
                    En 2017, les activités humaines et non humaines confondues au niveau mondial 
                    émettent environ mille cent tonnes de dioxyde de carbone en une seconde, soit un total annuel de 
                    36 800 000 000 000 kilogrammes de dioxyde de carbone.
                    
                    <br>
                    <br>
                    
                    Actuellement, dans un climat géopolitique, économique, social et environnemental extrêmement tendu 
                    pour la préservation de l'écosystème planétaire, l'Association devra poursuivre ses objectifs en 
                    encourageant le monde entier à participer volontairement à son marché volontaire de compensation 
                    carbone pour réduire la quantité de dioxyde de carbone dans l'atmosphère par le biais d'un registre 
                    de crédits carbone tenu par l'Association afin d'user de solutions innovantes telles que les 
                    technologies de capture de dioxyde de carbone depuis l'atmosphère et les techniques de 
                    séquestration artificielle de dioxyde de carbone dans le sol ou les sous-sols dont ces solutions 
                    innovantes seront proposées par des porteurs de projets en suivant une méthodologie stricte et 
                    transparente établie par l'Association pour garantir le bon accomplissement de la compensation 
                    carbone de manière sûr et pérenne, et le financement des projets sera exclusivement assuré par 
                    la vente de crédits carbone par les porteurs de projets aux acheteurs qui souhaiteront compenser 
                    volontairement leurs émissions de dioxyde de carbone.
                  </div>
                </div>
                <!-- Préambule  -->

                <br>
                <br>

                <!-- I - Nom, siège, but, moyens et ressources -->
                <div class="card text-center">
                  <div class="card-header">
                    I - Nom, siège, but, moyens et ressources
                  </div>
                  <div class="card-body">
                    <!-- Article 1 - Nom et durée -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 1 - Nom et durée
                      </div>
                      <div class="card-body">
                        Sous la dénomination de "Association MyTrapCoo" ci-après l’Association, est constituée une 
                        association de droit privé à buts de service public au sens des articles 60 et suivants du 
                        Code civil suisse. 
                        
                        <br>
                        <br>
                        
                        Sa durée est indéterminée.
                      </div>
                    </div>
                    <!--  Article 1 - Nom et durée -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 2 - Siège -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 2 - Siège
                      </div>
                      <div class="card-body">
                        L’Association a son siège dans le canton de Genève.
                      </div>
                    </div>
                    <!-- Article 2 - Siège -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 3 - But -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 3 - Buts
                      </div>
                      <div class="card-body">
                        L’Association a pour but de :
                        <br>
                        - Mettre en place un marché volontaire de compensation carbone pour réduire la quantité de 
                        dioxyde de carbone dans l'atmosphère,
                        <br>
                        - Rédiger une méthodologie claire et pratique des moyens à mettre en oeuvre pour l'évaluation 
                        des projets de capture et séquestration pérenne du dioxyde de carbone issu de l'atmosphère,
                        <br>
                        - Repérer des terrains pouvant accueillir des projets de capture de dioxyde de carbone 
                        atmosphérique et séquestration naturelle ou artificielle du dioxyde de carbone à travers 
                        le monde et en particulier dans des pays où la peine de mort est abolie et la demande 
                        d'autorisation d'exploiter une installation de production d'électricité pour les consommations 
                        propres est réputée autorisée quel que soit le type d'énergie primaire de l'installation, les 
                        machines installées dans l'installation et la puissance installée de l'installation, 
                        <br>
                        - Prospecter des fabricants de technologie de capture de dioxyde de carbone atmosphérique,
                        <br>
                        - Prospecter des fabricants de canalisations en béton armé,
                        <br>
                        - Prospecter des fabricants de matériaux de constructions,
                        <br>
                        - Prospecter des fabricants de machines à énergie libre,
                        <br>
                        - Prospecter des professionnels pour des conseils de faisabilité d'un projet de capture de 
                        dioxyde de carbone atmosphérique et séquestration naturelle ou artificielle du dioxyde de 
                        carbone,
                        <br>
                        - Valider l'inscription des dossiers des porteurs de projet de capture de dioxyde de carbone 
                        atmosphérique et séquestration naturelle ou artificielle du dioxyde de carbone,
                        <br>
                        - Émettre un crédit carbone par tonne de dioxyde de carbone capturé depuis l'atmosphère et 
                        séquestré dans les sols ou les sous-sols à un porteur de projet de capture de dioxyde de carbone 
                        atmosphérique et séquestration naturelle ou artificielle du dioxyde de carbone,
                        <br>
                        - Tenir un registre de crédits carbone pour assurer une traçabilité précise des crédits carbone 
                        émis sur ce marché volontaire de compensation carbone,
                        <br>
                        - Prospecter des acheteurs pour les encourager à compenser volontairement leurs émissions de 
                        dioxyde de carbone dans l'atmosphère,
                        <br>
                        - Valider l'inscription des dossiers des acheteurs de crédits carbone,
                        <br>
                        - Entretenir les dossiers des porteurs de projet et des acheteurs en toute sécurité et 
                        confidentialité,
                        <br>
                        - Assurer la vente de crédits carbone entre les porteurs de projet et les acheteurs pour 
                        éviter toute fraude que ce soit,
                        <br>
                        - Diffuser des informations disponibles au public concernant les différents projets, la 
                        quantité de dioxyde de carbone capturé depuis l'atmosphère et séquestré dans les sols ou les 
                        sous-sols par les différents projets, la quantité de crédits carbone émise et vendue et 
                        disponible sur ce marché volontaire de compensation carbone, le cours du crédit carbone sur 
                        ce marché volontaire de compensation carbone et le fonctionnement de l'Association.
                        
                        <br>
                        <br>
                        
                        L’Association n’a pas de but lucratif et a des buts de service public pour la protection de 
                        l'environnement au niveau mondial en faisant de la séquestration naturelle ou artificielle de 
                        dioxyde de carbone pour lutter contre le réchauffement climatique.
                        
                        <br>
                        <br>
                        
                        Conformément à l'article 74 du Code civil suisse, la transformation du but social de 
                        l'Association ne peut être imposée à aucun Membre.
                      </div>
                    </div>
                    <!-- Article 3 - But -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 4 - Moyens -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 4 - Moyens
                      </div>
                      <div class="card-body">
                        L’Association peut entreprendre toute activité licite propre à atteindre son but.
                        
                        <br>
                        <br>
                        
                        En particulier, l’Association pourra entreprendre ce qui suit :
                        <br>
                        - Développer un site internet pour détailler le but de l'Association,
                        <br>
                        - Développer un registre de crédits carbone avec une technologie de type "Blockchain",
                        <br>
                        - Développer des logiciels applicatifs licites affectés exclusivement à son but à caractère 
                        non lucratif et à caractère de service public,
                        <br>
                        - Acheter des biens immobiliers affectés exclusivement à son but à caractère non lucratif et 
                        à caractère de service public,
                        <br>
                        - Acheter des outils, des biens et des fournitures licites affectés exclusivement à 
                        son but à caractère non lucratif et à caractère de service public,
                        <br>
                        - Acheter des véhicules, des camions et des engins de manutention affectés exclusivement à 
                        son but à caractère non lucratif et à caractère de service public,
                        <br>
                        - Faire appel au bénévolat affecté exclusivement à son but à caractère non lucratif et à 
                        caractère de service public,
                        <br>
                        - Mener des études, des recherches et des développements sur des moyens pouvant être mis en 
                        place pour lutter contre le réchauffement climatique et affectés exclusivement à son but à 
                        caractère non lucratif et à caractère de service public.
                      </div>
                    </div>
                    <!-- Article 4 - Moyens -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 5 - Ressources -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 5 - Ressources
                      </div>
                      <div class="card-body">
                        Les ressources de l’Association pourront provenir de donations, legs, sponsors, partenariats, 
                        subsides publics, cotisations des Membres, revenus générés par les actifs de l’Association, 
                        ainsi que toute autre ressource légale.
                        
                        <br>
                        <br>
                        
                        Toutes les ressources de l’Association devront être affectées exclusivement à la réalisation 
                        de son but non-lucratif pour la protection de l'environnement à des fins de service public et 
                        d'utilité publique.
                      </div>
                    </div>
                    <!-- Article 5 - Ressources -->
                  </div>
                </div>
                <!-- I - Nom, siège, but, moyens et ressources -->

                <br>
                <br>

                <!-- II - Membres  -->
                <div class="card text-center">
                  <div class="card-header">
                    II - Membres
                  </div>
                  <div class="card-body">
                    <!-- Article 6 - Membres -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 6 - Membres
                      </div>
                      <div class="card-body">
                        Les membres de l’Association (les « Membres ») sont des individus ou des personnes morales 
                        qui ont un intérêt pour le but et les activités de l’Association et/ou qui souhaitent soutenir 
                        ceux-ci.
                      </div>
                    </div>
                    <!-- Article 6 - Membres -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 7 - Adhésion -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 7 - Adhésion
                      </div>
                      <div class="card-body">
                        Les fondateurs sont les Membres initiaux de l’Association. 
                        
                        <br>
                        <br>
                        
                        Conformément à l'alinéa 1 de l'article 70 du Code civil suisse, l'Association peut en tout 
                        temps recevoir de nouveaux membres.
                        
                        <br>
                        <br>
                        
                        Des Membres additionnels peuvent rejoindre l’Association en soumettant une demande écrite au 
                        Comité. 
                        
                        <br>
                        <br>
                        
                        Le Comité revoit les demandes d’adhésion avant de les soumettre à l’Assemblée générale pour 
                        approbation.
                      </div>
                    </div>
                    <!-- Article 7 - Adhésion -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 8 - Fin de l'adhésion -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 8 - Fin de l'adhésion
                      </div>
                      <div class="card-body">
                        Conformément à l'alinéa 2 de l'article 70 du Code civil suisse, chaque Membre est autorisé 
                        de par la loi à sortir de l’Association, pourvu que le Membre annonce sa sortie six mois avant 
                        la fin de l’année civile ou, lorsqu’un exercice administratif est prévu, six mois avant la fin 
                        de celui-ci.

                        <br>
                        <br>
                        
                        Conformément à l'alinéa 3 de l'article 70 du Code civil suisse, la qualité de Membre est 
                        inaliénable et ne passe point aux héritiers.

                        <br>
                        <br>
                        
                        L’adhésion d’un Membre se termine par :
                        <br>
                        - la démission du Membre adressée au Comité au moins six mois avant la fin de l’année civile 
                        en vertu de l'alinéa 2 de l'article 70 du Code civil suisse,
                        <br>
                        - si le Membre est un individu, au moment de son décès, la qualité de Membre étant inaliénable 
                        en vertu de l'alinéa 3 de l'article 70 du Code civil suisse,
                        <br>
                        - lors de l’exclusion du Membre sur décision de l’Assemblée générale, soit (1) pour les motifs 
                        suivants : le vol envers l'Association, la corruption envers l'Association, la divulgation 
                        d'informations confidentielles de l'Association à un tiers, le non-respect des statuts de 
                        l'Association, le désengagement de verser sa cotisation à l'Association, l'utilisation des 
                        biens et des ressources de l'Association à des fins personnelles, le blachiment d'argent 
                        en utilisant l'Association de quel que manière que ce soit, le recel en utilisant 
                        l'Association de quel que manière que ce soit, l'extorsion de fonds de l'Association, 
                        le chantage contre un autre Membre de l'Association, la sextorsion contre un autre Membre 
                        de l'Association, l'injure et l'outrage contre un autre Membre de l'Association, le meurtre 
                        contre un autre Membre de l'Association, l'enlèvement d'un autre Membre de l'Association, le 
                        cambriolage contre un autre Membre de l'Association, le vol contre un autre Membre de 
                        l'Association, le cambriolage contre l'Association, l'agression sexuelle contre un autre 
                        Membre de l'Association ou (2) sans indication des motifs.
                        
                        <br>
                        <br>
                        
                        Conformément à l'alinéa 1 de l'article 73 du Code civil suisse, un Membre démissionnaire 
                        ou exclu n’a aucun droit à l’avoir social de l’Association.
                        
                        <br>
                        <br>
                        
                        Conformément à l'alinéa 2 de l'article 73 du Code civil suisse, dans tous les cas, 
                        la cotisation de l’année en cours reste due par le Membre sortant.
                      </div>
                    </div>
                    <!-- Article 8 - Fin de l'adhésion -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 9 - Cotisations -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 9 - Cotisations
                      </div>
                      <div class="card-body">
                        Conformément à l'article 71 du Code civil suisse, les Membres de l'Association sont tenus de 
                        verser des cotisations.
                        
                        <br>
                        <br>
                        
                        L’Assemblée générale décide du principe et du montant des cotisations des Membres.
                      </div>
                    </div>
                    <!-- Article 9 - Cotisations -->
                  </div>
                </div>
                <!-- II - Membres -->

                <br>
                <br>

                <!-- III - Organisation et gouvernance -->
                <div class="card text-center">
                  <div class="card-header">
                    III - Organisation et gouvernance
                  </div>
                  <div class="card-body">
                    <!-- Article 10 - Organes de l'association -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 10 - Organes de l'association
                      </div>
                      <div class="card-body">
                        Les organes de l’Association sont :
                        <br>
                        - l’Assemblée générale,
                        <br>
                        - le Comité,
                        <br>
                        - les Auditeurs externes, dans la mesure où cela est requis par le droit suisse.
                      </div>
                    </div>
                    <!-- Article 10 - Organes de l'association -->
                  </div>
                </div>
                <!-- III - Organisation et gouvernance -->

                <br>
                <br>

                <!-- IV - L'assemblée générale -->
                <div class="card text-center">
                  <div class="card-header">
                    IV - L'assemblée générale
                  </div>
                  <div class="card-body">
                    <!-- Article 11 - Principes -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 11 - Principes
                      </div>
                      <div class="card-body">
                        Conformément à l'alinéa 1 de l'article 64 du Code civil suisse, l’Assemblée générale 
                        constitue le pouvoir suprême de l’Association.
                        
                        <br>
                        <br>
                        
                        L'Assemblée générale est composée de tous les Membres.
                        
                        <br>
                        <br>
                        
                        Conformément à l'alinéa 2 de l'article 64 du Code civil suisse, l'Assemblée générale est 
                        convoquée par le Comité.
                        
                        <br>
                        <br>
                        
                        Conformément à l'alinéa 3 de l'article 64 du Code civil suisse, la convocation de l'Assemblée 
                        générale a lieu dans les cas prévus par les statuts et en outre, de par la loi, lorsque le 
                        cinquième des Membres en fait la demande.
                      </div>
                    </div>
                    <!-- Article 11 - Principes -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 12 - Pouvoirs -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 12 - Pouvoirs
                      </div>
                      <div class="card-body">
                        Vu l'article 65 du Code civil suisse,
                        
                        <br>
                        <br>
                        
                        Conformément à l'alinéa 1 de l'article 65 du Code civil suisse, l’Assemblée générale 
                        délègue au Comité les pouvoirs de gérer et de représenter l’Association. 
                        
                        <br>
                        <br>
                        
                        Conformément aux alinéas de l'article 65 du Code civil suisse, l’Assemblée générale 
                        conserve les pouvoirs inaliénables suivants :
                        <br>
                        - adoption et modification des Statuts,
                        <br>
                        - nomination, surveillance et révocation des Auditeurs externes,
                        <br>
                        - approbation des rapports annuels, des comptes non audités et des comptes audités,
                        <br>
                        - admission et exclusion des Membres,
                        <br>
                        - nomination, surveillance, décharge et révocation des membres du Comité,
                        <br>
                        - décision de dissolution ou de fusion de l’Association,
                        <br>
                        - gestion de toutes les affaires qui ne sont pas du ressort d’autres organes,
                        <br>
                        - révocation existante de par la loi lorsqu'il est exercé pour de justes motifs.
                      </div>
                    </div>
                    <!-- Article 12 - Pouvoirs -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 13 - Réunions -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 13 - Réunions
                      </div>
                      <div class="card-body">
                        <!-- Assemblée générale ordinaire -->
                        <div class="card text-center">
                          <div class="card-header">
                             Assemblée générale ordinaire
                          </div>
                          <div class="card-body">
                            L’Assemblée générale ordinaire se tient au moins une fois par an, en personne.
                          </div>
                        </div>
                        <!-- Assemblée générale ordinaire -->
                        
                        <br>
                        <br>
                        
                        <!-- Assemblée générale extraordinaire -->
                        <div class="card text-center">
                          <div class="card-header">
                             Assemblée générale extraordinaire
                          </div>
                          <div class="card-body">
                            Des Assemblées générales extraordinaires peuvent être tenues à la demande du Comité ou 
                            d’au moins vingt pour cent des Membres, conformément à l'alinéa 3 de l’article 64 du Code 
                            civil suisse.
                          </div>
                        </div>
                        <!-- Assemblée générale extraordinaire -->
                        
                        <br>
                        <br>
                        
                        <!-- Convocation -->
                        <div class="card text-center">
                          <div class="card-header">
                             Convocation
                          </div>
                          <div class="card-body">
                            Le Comité convoque les réunions de l’Assemblée générale quarante jours à l’avance. 
                            
                            <br>
                            <br>
                            
                            L’ordre du jour des réunions doit être transmis avec les convocations. Les convocations 
                            peuvent être envoyées par courrier ou e-mail.
                            
                            <br>
                            <br>
                            
                            L'ordre du jour des réunions doit contenir au minimum les points suivants :
                            <br>
                            - l'approbation du procès-verbal de la précédente assemblée générale,
                            <br>
                            - un rapport du comité sur les activités,
                            <br>
                            - un rapport sur les finances,
                            <br>
                            - les élections nécessaires au Comité et au sein de l'organe de révision.
                          </div>
                        </div>
                        <!-- Convocation -->
                        
                        <br>
                        <br>
                        
                        <!-- Quorum -->
                        <div class="card text-center">
                          <div class="card-header">
                             Quorum
                          </div>
                          <div class="card-body">
                            L’Assemblée générale est valablement constituée à condition d'avoir au moins vingt pour 
                            cent des Membres présents lors de la réunion.
                          </div>
                        </div>
                        <!-- Quorum -->
                        
                        <br>
                        <br>
                        
                        <!-- Présidence -->
                        <div class="card text-center">
                          <div class="card-header">
                             Présidence
                          </div>
                          <div class="card-body">
                            Le/la Président(e) et en son absence le/la Vice-Président(e), tels que définis à 
                            l’article 17 ci-après, présidera les réunions de l’Assemblée générale.
                          </div>
                        </div>
                        <!-- Présidence -->
                      </div>
                    </div>
                    <!-- Article 13 - Réunions -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 14 - Décisions et droits de vote -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 14 - Décisions et droits de vote
                      </div>
                      <div class="card-body">
                        <!-- Droit de vote -->
                        <div class="card text-center">
                          <div class="card-header">
                             Droit de vote
                          </div>
                          <div class="card-body">
                            Conformément à l'alinéa 1 de l'article 67 du Code civil suisse, tous les Membres ont 
                            un droit de vote égal au sein de l’Assemblée générale.
                          </div>
                        </div>
                        <!-- Droit de vote -->
                        
                        <br>
                        <br>
                        
                        <!-- Procuration -->
                        <div class="card text-center">
                          <div class="card-header">
                             Procuration
                          </div>
                          <div class="card-body">
                            Les Membres peuvent être représentés par une procuration accordée à un tiers n'étant 
                            pas Membre de l'Association.
                          </div>
                        </div>
                        <!-- Procuration -->
                        
                        <br>
                        <br>
                        
                        <!-- Mode -->
                        <div class="card text-center">
                          <div class="card-header">
                             Mode
                          </div>
                          <div class="card-body">
                            Conformément à l'alinéa 1 de l'article 66 du Code civil suisse, les décisions de 
                            l'association sont prises en assemblée générale, et les votes ont lieu à main levée.
                            
                            <br>
                            <br>
                            
                            À la demande d’un cinquième des Membres au moins, ils peuvent avoir lieu à bulletin secret.
                          </div>
                        </div>
                        <!-- Mode -->
                        
                        <br>
                        <br>
                        
                        <!-- Majorités -->
                        <div class="card text-center">
                          <div class="card-header">
                             Majorités
                          </div>
                          <div class="card-body">
                            Conformément à l'alinéa 2 de l'article 67 du Code civil suisse, les décisions de 
                            l’Assemblée générale sont prises à la majorité des votes exprimés par des Membres présents, 
                            y compris ceux votant par l’intermédiaire d’une procuration, pour autant que les 
                            présents Statuts ne prévoient pas une majorité différente.
                            
                            <br>
                            <br>
                            
                            Conformément à l'alinéa 3 de l'article 67 du Code civil suisse, les décisions de 
                            l'Assemblée générale ne peuvent être prises en dehors de l'ordre du jour.
                          </div>
                        </div>
                        <!-- Majorités -->
                        
                        <br>
                        <br>
                        
                        <!-- Décision circulaire -->
                        <div class="card text-center">
                          <div class="card-header">
                             Décision circulaire
                          </div>
                          <div class="card-body">
                            Les propositions auxquelles tous les Membres ont adhéré par écrit équivalent à des 
                            décisions de l’Assemblée générale, conformément à l'alinéa 2 de l’article 66 du Code civil 
                            suisse.
                          </div>
                        </div>
                        <!-- Décision circulaire -->
                        
                        <br>
                        <br>
                        
                        <!-- Conflit d’intérêt -->
                        <div class="card text-center">
                          <div class="card-header">
                             Conflit d'intérêt
                          </div>
                          <div class="card-body">
                            Conformément à l’article 68 du Code civil suisse, un Membre ne peut voter pour les 
                            décisions relatives à une affaire ou un procès de l’Association, lorsque lui-même, 
                            son conjoint ou ses parents ou alliés en ligne directe sont parties en cause.
                          </div>
                        </div>
                        <!-- Conflit d’intérêt -->
                        
                        <br>
                        <br>
                        
                        <!-- Procès-verbaux -->
                        <div class="card text-center">
                          <div class="card-header">
                             Procès-verbaux
                          </div>
                          <div class="card-body">
                            Les réunions de l’Assemblée générale et ses décisions sont retranscrites dans 
                            des procès-verbaux.
                          </div>
                        </div>
                        <!-- Procès-verbaux -->
                      </div>
                    </div>
                    <!-- Article 14 - Décisions et droits de vote -->
                  </div>
                </div>
                <!-- IV - L'assemblée générale -->

                <br>
                <br>
                
                <!-- V - Le comité -->
                <div class="card text-center">
                  <div class="card-header">
                    V - Le comité
                  </div>
                  <div class="card-body">
                    <!-- Article 15 - Principes -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 15 - Principes
                      </div>
                      <div class="card-body">
                        <!-- Rôle et pouvoirs -->
                        <div class="card text-center">
                          <div class="card-header">
                             Rôle et pouvoirs
                          </div>
                          <div class="card-body">
                            Le Comité est l’organe exécutif de l’Association.
                            
                            <br>
                            <br>
                            
                            Conformément à l'article 69 du Code civil suisse, le Comité a le droit et le devoir de 
                            gérer les affaires de l’Association et de la représenter en conformité des Statuts.
                            
                            <br>
                            <br>
                            
                            Le Comité doit notamment, prendre toute mesure utile pour atteindre le but de 
                            l'Association, veiller à l'application correcte des présents Statuts et d'autres 
                            éventuels règlements internes, administrer les biens, actifs et ressources de 
                            l’Association, tenir la comptabilité, engager et superviser un(e) directeur(rice), 
                            si nécessaire, et convoquer et organiser l'Assemblée générale.
                          </div>
                        </div>
                        <!-- Rôle et pouvoirs -->
                        
                        <br>
                        <br>
                        
                        <!-- Bénévolat -->
                        <div class="card text-center">
                          <div class="card-header">
                             Bénévolat
                          </div>
                          <div class="card-body">
                            Les membres du Comité agissent bénévolement et ne peuvent prétendre qu’à l’indemnisation 
                            de leurs frais effectifs et de leurs frais de déplacement. 
                            
                            <br>
                            <br>
                            
                            Des éventuels jetons de présence ne peuvent excéder ceux versés pour des commissions 
                            officielles de l’Etat de Genève.
                            
                            <br>
                            <br>
                            
                            Pour les activités qui excèdent le cadre usuel de la fonction, chaque membre du Comité 
                            peut recevoir un dédommagement approprié.
                            
                            <br>
                            <br>
                            
                            Les employé(es) rémunéré(es) de l’Association ne peuvent siéger au Comité qu’avec une voix 
                            consultative.
                          </div>
                        </div>
                        <!-- Bénévolat -->
                      </div>
                    </div>
                    <!-- Article 15 - Principes -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 16 - Nomination du comité -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 16 - Nomination du comité
                      </div>
                      <div class="card-body">
                        Le Comité initial est élu par les membres fondateurs.
                        
                        <br>
                        <br>
                        
                        Après cela, les nouveaux membres du Comité sont élus par l’Assemblée générale en vertu de 
                        l'article 65 du Code civil suisse.
                      </div>
                    </div>
                    <!-- Article 16 - Nomination du comité -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 17 - Composition -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 17 - Composition
                      </div>
                      <div class="card-body">
                        Le Comité se compose d’au moins cinq et d’au maximum onze membres.
                        
                        <br>
                        <br>
                        
                        Le Comité désigne en son sein le/la Président(e), le/la Vice-Président(e), ainsi que toute autre 
                        fonction qu’il jugera utile.
                        
                        <br>
                        <br>
                        
                        Au moins un membre du Comité, avec pouvoir de signature est un(e) citoyen(ne) suisse ou 
                        citoyen(ne) d’un Etat membre de l’Union Européenne ou l'Association européenne de libre-échange 
                        et résident(e) en Suisse.
                      </div>
                    </div>
                    <!-- Article 17 - Composition -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 18 - Durée du mandat -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 18 - Durée du mandat
                      </div>
                      <div class="card-body">
                        Les membres du Comité sont nommés pour des mandats de quatre ans, renouvelables au maximum 
                        deux fois.
                      </div>
                    </div>
                    <!-- Article 18 - Durée du mandat -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 19 - Révocation et démission -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 19 - Révocation et démission
                      </div>
                      <div class="card-body">
                        <!-- Révocation -->
                        <div class="card text-center">
                          <div class="card-header">
                             Révocation
                          </div>
                          <div class="card-body">
                            Le mandat d’un membre du Comité peut être révoqué par l’Assemblée générale, 
                            en particulier s’il ou elle a violé ses obligations à l’encontre de l’Association ou 
                            s’il ou elle n’est pas en mesure d’exercer correctement ses fonctions.
                          </div>
                        </div>
                        <!-- Révocation -->
                        
                        <br>
                        <br>
                        
                        <!-- Démission -->
                        <div class="card text-center">
                          <div class="card-header">
                             Démission
                          </div>
                          <div class="card-body">
                            Les membres du Comité peuvent démissionner en tout temps en soumettant une déclaration 
                            écrite au/à la Président(e) du Comité, précisant la date à laquelle leur démission 
                            prendra effet.
                          </div>
                        </div>
                        <!-- Démission -->
                        
                        <br>
                        <br>
                        
                        <!-- Vacances en cours de mandat -->
                        <div class="card text-center">
                          <div class="card-header">
                             Vacances en cours de mandat
                          </div>
                          <div class="card-body">
                            En cas de révocation ou de démission en cours de mandat, le Comité peut nommer un membre 
                            remplaçant par cooptation, jusqu’à la prochaine Assemblée générale.
                          </div>
                        </div>
                        <!-- Vacances en cours de mandat -->
                      </div>
                    </div>
                    <!-- Article 19 - Révocation et démission -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 20 - Délégation et représentation -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 20 - Délégation et représentation
                      </div>
                      <div class="card-body">
                        <!-- Délégation -->
                        <div class="card text-center">
                          <div class="card-header">
                             Délégation
                          </div>
                          <div class="card-body">
                            Le Comité est autorisé à déléguer certaines de ses tâches à un ou plusieurs de ses 
                            membres y compris à des sous-comités, à des tiers qu’il mandate ou à des employé(es) 
                            qu’il engage.
                          </div>
                        </div>
                        <!-- Délégation -->
                        
                        <br>
                        <br>
                        
                        <!-- Représentation -->
                        <div class="card text-center">
                          <div class="card-header">
                             Représentation
                          </div>
                          <div class="card-body">
                            L’Association est valablement représentée et engagée par la signature collective de deux 
                            membres de son Comité et/ou tout(e) autre dirigeant(e) ou représentant(e) désigné(e) à cet 
                            effet par le Comité dans une procuration.
                          </div>
                        </div>
                        <!-- Représentation -->
                      </div>
                    </div>
                    <!-- Article 20 - Délégation et représentation -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 21 - Réunions -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 21 - Réunions
                      </div>
                      <div class="card-body">
                        <!-- Réunion -->
                        <div class="card text-center">
                          <div class="card-header">
                             Réunion
                          </div>
                          <div class="card-body">
                            Le Comité se réunit aussi souvent que nécessaire, mais au moins deux fois par an.
                          </div>
                        </div>
                        <!-- Réunion -->
                        
                        <br>
                        <br>
                        
                        <!-- Mode -->
                        <div class="card text-center">
                          <div class="card-header">
                             Mode
                          </div>
                          <div class="card-body">
                            Les membres du Comité peuvent valablement participer à une réunion du Comité et prendre 
                            des décisions par vidéo ou conférence téléphonique ou en personne.
                          </div>
                        </div>
                        <!-- Mode -->
                        
                        <br>
                        <br>
                        
                        <!-- Convocation -->
                        <div class="card text-center">
                          <div class="card-header">
                             Convocation
                          </div>
                          <div class="card-body">
                            Le/la Président(e) du Comité convoque les réunions du Comité au moins vingt jours à 
                            l’avance.
                            
                            <br>
                            <br>
                            
                            Si des circonstances urgentes le justifient, le/la Président(e) peut convoquer une réunion 
                            extraordinaire avec un préavis de huit jours.
                          </div>
                        </div>
                        <!-- Convocation -->
                      </div>
                    </div>
                    <!-- Article 21 - Réunions -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 22 - Prise de décision -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 22 - Prise de décision
                      </div>
                      <div class="card-body">
                        <!-- Voix et Majorités -->
                        <div class="card text-center">
                          <div class="card-header">
                             Voix et Majorités
                          </div>
                          <div class="card-body">
                            Chaque membre du Comité dispose d’une voix.
                            
                            <br>
                            <br>
                            
                            Les décisions sont prises à la majorité simple des membres présents, pour autant que les 
                            présents Statuts de l’Association ne prévoient pas d’autres majorités. 
                            
                            <br>
                            <br>
                            
                            En cas d’égalité des voix, le/la Président(e) dispose d’une voix prépondérante.
                          </div>
                        </div>
                        <!-- Voix et Majorités -->
                        
                        <br>
                        <br>
                        
                        <!-- Décisions circulaires -->
                        <div class="card text-center">
                          <div class="card-header">
                             Décisions circulaires
                          </div>
                          <div class="card-body">
                            Les décisions du Comité peuvent aussi valablement être prises par voie de circulaire, 
                            y compris par email.
                          </div>
                        </div>
                        <!-- Décisions circulaires -->
                        
                        <br>
                        <br>
                        
                        <!-- Procès-verbaux -->
                        <div class="card text-center">
                          <div class="card-header">
                             Procès-verbaux
                          </div>
                          <div class="card-body">
                            Les réunions du Comité et ses décisions sont retranscrites dans des procès-verbaux.
                          </div>
                        </div>
                        <!-- Procès-verbaux -->
                      </div>
                    </div>
                    <!-- Article 22 - Prise de décision -->
                  </div>
                </div>
                <!-- V - Le comité -->

                <br>
                <br>
                
                <!-- VI - Dispositions diverses et finales -->
                <div class="card text-center">
                  <div class="card-header">
                    VI - Dispositions diverses et finales
                  </div>
                  <div class="card-body">
                    <!-- Article 23 - Secrétariat -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 23 - Secrétariat
                      </div>
                      <div class="card-body">
                        Le Comité peut établir un secrétariat et/ou nommer un(e) directeur(rice) afin de gérer les 
                        affaires courantes de l’Association.
                      </div>
                    </div>
                    <!-- Article 23 - Secrétariat -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 24 - Organe de révision -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 24 - Organe de révision
                      </div>
                      <div class="card-body">
                        <!-- Organe obligatoire -->
                        <div class="card text-center">
                          <div class="card-header">
                             Organe obligatoire
                          </div>
                          <div class="card-body">
                            En vertu de l'alinéa 1 de l'article 69b du Code civil suisse, dans la mesure où cela est 
                            requis par le droit suisse, l’Assemblée générale nomme un organe de révision externe et 
                            indépendant (auditeur) chargé (1) de vérifier les comptes annuels de l’Association et de 
                            soumettre un rapport détaillé à l’Assemblée générale et (2) de s’assurer que les règles 
                            statutaires de l’Association (Statuts et règlements internes) soient respectées.
                            
                            <br>
                            <br>
                            
                            Conformément à l'alinéa 3 de l'article 69b du Code civil suisse, les dispositions du code 
                            des obligations concernant l'organe de révision de la société anonyme sont applicables par 
                            analogie.
                          </div>
                        </div>
                        <!-- Organe obligatoire -->
                        
                        <br>
                        <br>
                        
                        <!-- Organe facultatif -->
                        <div class="card text-center">
                          <div class="card-header">
                             Organe facultatif
                          </div>
                          <div class="card-body">
                            Conformément à l'alinéa 4 de l'article 69b du Code civil suisse, les Statuts et l'Assemblée 
                            générale peuvent organiser le contrôle librement.
                            
                            <br>
                            <br>
                             
                            L’Association qui n’est pas soumise à l’obligation de nommer un organe de révision 
                            externe peut néanmoins décider de nommer un (ou plusieurs) vérificateur(s) des comptes, 
                            indépendant(s) du Comité, qui devra/devront établir un rapport à l’attention de 
                            l’Assemblée générale.
                          </div>
                        </div>
                        <!-- Organe facultatif -->
                      </div>
                    </div>
                    <!-- Article 24 - Organe de révision -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 25 - Comptabilité -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 25 - Comptabilité
                      </div>
                      <div class="card-body">
                        <!-- Comptes -->
                        <div class="card text-center">
                          <div class="card-header">
                             Comptes
                          </div>
                          <div class="card-body">
                            Conformément à l'article 69a du Code civil suisse, le Comité tient les livres de 
                            l'Association. Les dispositions du code des obligations relatives à la comptabilité 
                            commerciale et à la présentation des comptes sont applicables par analogie.
                            
                            <br>
                            <br>
                            
                            Conformément à l'alinéa 2 de l'article 957 du Code des obligations du droit suisse, 
                            l'Association ne tienne qu'une comptabilité des recettes et des dépenses ainsi que du 
                            patrimoine puisque l'Association n'a pas l'obligation de requérir son inscription auprès du 
                            registre du commerce.
                            
                            <br>
                            <br>
                            
                            Le Comité établit les comptes pour chaque année comptable, tel que cela est requis par le 
                            droit applicable.
                          </div>
                        </div>
                        <!-- Comptes -->
                        
                        <br>
                        <br>
                        
                        <!-- Exercice -->
                        <div class="card text-center">
                          <div class="card-header">
                             Exercice
                          </div>
                          <div class="card-body">
                            L’exercice comptable débute le 1er janvier et prend fin le 31 décembre de chaque année.
                          </div>
                        </div>
                        <!-- Exercice -->
                      </div>
                    </div>
                    <!-- Article 25 - Comptabilité -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 26 - Responsabilité -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 26 - Responsabilité
                      </div>
                      <div class="card-body">
                        Conformément à l'article 75a du Code civil suisse, l’Association répond seule de ses dettes, 
                        qui sont garanties par sa fortune sociale.
                        
                        <br>
                        <br>
                        
                        Les Membres n’ont aucune responsabilité personnelle pour les dettes de l’Association.
                      </div>
                    </div>
                    <!-- Article 26 - Responsabilité -->
                    
                    <br>
                    <br>
                    
                    <!-- Article 27 - Dissolution -->
                    <div class="card text-center">
                      <div class="card-header">
                         Article 27 - Dissolution
                      </div>
                      <div class="card-body">
                        Conformément à l'article 76 du Code civil suisse, l'Association peut décider sa dissolution en 
                        tout temps, et la dissolution de l’Association ne peut être décidée qu’à un vote à la majorité 
                        des deux-tiers de tous les Membres.
                        
                        <br>
                        <br>
                        
                        Conformément à l'article 77 du Code civil suisse, l'Association est dissoute de plein droit 
                        lorsque l'Association est insolvable ou lorsque le Comité ne peut plus être constitué 
                        statutairement.
                        
                        <br>
                        <br>
                        
                        Conformément à l'article 78 du Code civil suisse, la dissolution de l'Association est 
                        prononcée par le juge, à la demande de l'autorité compétente ou d'un intéressé, lorsque le 
                        but de l'association est illicite ou contraire aux mœurs.

                        <br>
                        <br>
                        
                        Conformément à l'article 79 du Code civil suisse, si l'Association est inscrite au registre du 
                        commerce, la dissolution de l'Association est déclarée par le Comité ou par le juge au préposé 
                        chargé de radier.
                        
                        <br>
                        <br>
                        
                        Dans ce cas, le Comité procède à la liquidation de l’Association.
                        
                        <br>
                        <br>
                        
                        Les actifs de l’Association serviront en premier lieu à l’extinction de ses dettes.
                        
                        <br>
                        <br>
                        
                        Le reliquat sera versé à une institution à but non-lucratif poursuivant un but d’intérêt 
                        public analogue à celui de l’association et bénéficiant de l’exonération de l’impôt.
                        
                        <br>
                        <br>

                        En aucun cas, les biens ne pourront retourner aux fondateurs physiques ou aux membres, 
                        ni être utilisés à leur profit en tout ou partie et de quelque manière que ce soit.
                      </div>
                    </div>
                    <!-- Article 27 - Dissolution -->
                  </div>
                </div>
                <!-- VI - Dispositions diverses et finales -->

                <br>
                <br>
                
                <!-- Acceptation des statuts de l'association à buts de service public MyTrapCoo -->
                <div class="card text-center">
                  <div class="card-header">
                    Acceptation des statuts de l'association à buts de service public MyTrapCoo
                  </div>
                  <div class="card-body">
                    Le 04 Avril 2022, l’assemblée constituante s'est tenue à Genève (1208) en Suisse.

                    <br>
                    <br>
                    
                    Bon pour acceptation des fonctions de Président de l’assemblée constitutive de l'association à 
                    buts de service public MyTrapCoo par Monsieur .
                    
                    <br>
                    <br>
                    
                    Bon pour acceptation des fonctions de Secrétaire de l’assemblée constitutive de l'association à 
                    buts de service public MyTrapCoo par Monsieur .
                    
                    <br>
                    <br>

                    En 5 exemplaires originaux pour le dépôt d'un exemplaire original au domicile du Président de 
                    l'association à buts de service public MyTrapCoo et l'exécution des diverses formalités légales 
                    pour le compte de l'association à buts de service public MyTrapCoo.

                    <br>
                    <br>
                    
                    Visé par Monsieur , Président de l’assemblée constitutive 
                    de l'association à buts de service public MyTrapCoo.

                    <br>
                    <br>

                    Apposition de la signature du Président de l'association à buts de service public MyTrapCoo 
                    précédée de la mention «Lu et approuvé» en bas de page de la dernière page des statuts de 
                    l'association à buts de service public MyTrapCoo.
                  </div>
                </div>
                <!-- Acceptation des statuts de l'association à buts de service public MyTrapCoo -->

                <br>
                <br>

              </div>
            </div>

            <br>
            <br>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" 
            crossorigin="anonymous"></script>
          </body>
        </html>
        """

        options = {
            'page-size': 'A4',
            'header-center': "Les statuts de l'association à buts de service public MyTrapCoo",
            'footer-left': '[page] sur [topage]'
        }

        path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        pdfkit.from_string(body,
                           "Association_MyTrapCoo\\Statuts_De_L_Association_MyTrapCoo.pdf",
                           configuration=config,
                           options=options)

        filename = "Association_MyTrapCoo\\Statuts_De_L_Association_MyTrapCoo.pdf"

        date_of_today = dt.today().strftime('%d_%m_%Y')

        filename_to_sign = filename.split(".pdf")[0] + "_" + date_of_today + ".pdf"

        try:
            packet = io.BytesIO()

            # create a new PDF with Reportlab
            can = canvas.Canvas(packet, pagesize=letter)

            can.setFontSize(8)

            x_coord = 5.9 * 72

            y_coord = 0.14 * 72

            date_of_signature = dt.today().strftime('%d/%m/%Y')

            # Insérer la valeur "Fait à ... (), le dd/mm/YYYY.".
            can.drawString(x_coord, y_coord, "Fait à Genève (1208) en Suisse, le " + date_of_signature + ".")

            # Insérer la valeur "Lu et approuvé.".
            can.drawString(x_coord, y_coord - 8, "Lu et approuvé.")

            can.save()

            # move to the beginning of the StringIO buffer
            packet.seek(0)

            new_pdf = PdfFileReader(packet)

            # read your existing PDF
            existing_pdf = PdfFileReader(open(filename, "rb"))

            page_number = existing_pdf.getNumPages()

            output = PdfFileWriter()

            # add the "text" (which is the new pdf) on the existing page
            last_page = existing_pdf.getPage(page_number - 1)

            last_page.mergePage(new_pdf.getPage(0))

            # add every pages of existing_pdf except the last page to output
            for i in range(0, page_number - 1):
                output.addPage(existing_pdf.getPage(i))

            output.addPage(last_page)

            # finally, write "output" to a real file
            output_stream = open(filename_to_sign, "wb")

            output.write(output_stream)

            output_stream.close()

            signature = "A:\\2_Personnel\\2_Non_Recurrentes\\62_Sign\\ma_signature_v2.png"

            pdf = PdfFileReader(open(filename_to_sign, 'rb'))

            page_number = pdf.getNumPages()

            x_coord = 4.4 * 72

            y_coord = 0.03 * 72

            width = 100

            height = round(0.55 * 72)

            os.system("signpdf " + str(filename_to_sign) + " " + str(signature) + " --coords " + str(page_number) + "x"
                      + str(round(x_coord)) + "x" + str(round(y_coord)) + "x" + str(width) + "x" + str(height))
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
