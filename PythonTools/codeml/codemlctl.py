class Config:
    
    def __new__(cls):
        return super().__new__(cls)

    def __init__ (self):
        self._settings = {"seqfile":["","","\t\t* sequence data filename",True,True], 
                "outfile":["","","\t\t* main result file name",True,True],
                "treefile":["","","\t\t* tree structure file name",True,True],
                "noisy":["","","\t\t* 0,1,2,3,9: how much rubbish on the screen",True,True],
                "verbose":["","","\t\t* 1: detailed output, 0: concise output",True,True],
                "runmode":["","","\t\t* 0: user tree; 1: semi-automatic; 2: automatic\n"
                                "\t\t\t* 3: StepwiseAddition; (4,5):PerturbationNNI; -2: pairwise\n",True,True],
                "seqtype":["","","\t\t* 1:codons; 2:AAs; 3:codons-->AAs",True,True],
                "CodonFreq":["","","\t\t* 0:1/61 each, 1:F1X4, 2:F3X4, 3:codon table",True,True],
                "ndata":["","","\t\t* Number of loci (or site partitions) in a combined analysis",True,True],
                "clock":["","","\t\t* 0:no clock, 1:clock; 2:local clock",True,True],
                "aaDist":["","","\t\t* 0:equal, +:geometric; -:linear, 1-6:G1974,Miyata,c,p,v,a\n"\
                                "\t\t\t* 7:AAClasses\n",True,True],
                "aaRatefile":["","","\t\t* only used for aa seqs with model=empirical(_F)\n"\
                                "\t\t\t* dayhoff.dat, jones.dat, wag.dat, mtmam.dat, or your own\n",True,True],
                "model":["","","\t\t* models for codons:\n"\
                                "\t\t\t* 0:one, 1:b, 2:2 or more dN/dS ratios for branches\n"\
                                "\t\t\t* models for AAs or codon-translated AAs:\n"\
                                "\t\t\t* 0:poisson, 1:proportional,2:Empirical,3:Empirical+F\n"\
                                "\t\t\t* 5:FromCodon0, 6:FromCodon1, 8:REVaa_0, 9:REVaa(nr=189)\n",True,True],
                "NSsites":["","","\t\t* 0:one w;1:neutral;2:selection; 3:discrete;4:freqs;\n"\
                                "\t\t\t* 5:gamma;6:2gamma;7:beta;8:beta&w;9:beta&gamma;\n"
                                "\t\t\t* 10:beta&gamma+1; 11:beta&normal>1; 12:0&2normal>1;\n"
                                "\t\t\t* 13:3normal>0\n",True,True],
                "icode":["","","\t\t* 0:universal code; 1:mammalian mt; 2-11:see manual",True,True],
                "Mgene":["","","\t\t* 0:rates, 1:separate;",True,True],
                "fix_kappa":["","","\t\t* 1: kappa fixed, 0: kappa to be estimated",True,True],
                "kappa":["","","\t\t* initial or fixed kappa",True,True],
                "fix_omega":["","","\t\t* 1: omega or omega_1 fixed, 0: estimate",True,True],
                "omega":["","","\t\t* initial or fixed omega, for codons or codon-based AAs",True,True],
                "fix_alpha":["","","\t\t* 0: estimate gamma shape parameter; 1: fix it at alpha",True,True],
                "alpha":["","","\t\t* initial or fixed alpha, 0:infinity (constant rate)",True,True],
                "Malpha":["","","\t\t* different alphas for genes",True,True],
                "ncatG":["","","\t\t* # of categories in dG of NSsites models",True,True],
                "fix_rho":["","","\t\t* 0: estimate rho; 1: fix it at rho",True,True],
                "rho":["","","\t\t* initial or fixed rho, 0:no correlation",True,True],
                "getSE":["","","\t\t* 0: don't want them, 1: want S.E.s of estimates",True,True],
                "RateAncestor":["","","\t\t* (0,1,2): rates (alpha>0) or ancestral states (1 or 2)",True,True],
                "Small_Diff":["",".5e-6","\t\t* Default .5e-6",True,True],
                "cleandata":["","","\t\t* remove sites with ambiguity data (1:yes, 0:no)?",True,True],
                "fix_blength":["","","\t\t* 0: ignore, -1: random, 1: initial, 2: fixed, 3: proportional",True,True],
                "method":["","","\t\t* 0: simultaneous; 1: one branch at a time",True,True]}
    
    def settings(self):
        return self._settings   

    def setModel(self,model:str,ncatG=""):
        if model == "M0":
            self.set("model","0")
            self.set("NSsites","0")
            self.remove("ncatG")
        elif model == "M1a":
            self.set("model","0")
            self.set("NSsites","1")
            self.remove("ncatG")
        elif model == "M2a":
            self.set("model","0")
            self.set("NSsites","2")
            self.remove("ncatG")
        elif model == "M3":
            self.set("model","0")
            self.set("NSsites","3")
            self.add("ncatG")
            if (ncatG==""):
                ncatG = 3
            self.set("ncatG",ncatG)
        elif model == "M7":
            self.set("model","0")
            self.set("NSsites","7")
            self.add("ncatG")
            if (ncatG==""):
                ncatG = 10
            self.set("ncatG",ncatG)
        elif model == "M8":
            self.set("model","0")
            self.set("NSsites","8")
            self.add("ncatG")
            if (ncatG==""):
                ncatG = 11
            self.set("ncatG",ncatG)
    def set(self, key:str, value:str):
        if key in self._settings:
            self._settings[str(key)][1] = value
        else:
            print(f'No key "{key}" found in settings')

    def silence(self, key:str):
        if key in self._settings:
            self._settings[key][0] = "*"
        else:
            print(f'No key "{key}" found in settings')

    def unsilence(self, key:str):
        if key in self._settings:
            self._settings[key][0] = ""
        else:
            print(f'No key "{key}" found in settings')

    def remove (self, key:str):
        if key in self._settings:
            self._settings[key][-1] = False
        else:
            print(f'No key "{key}" found in settings')

    def add(self, key:str):
        if key in self._settings:
            self._settings[key][-1] = True
        else:
            print(f'No key "{key}" found in settings')

    def disableComments(self, key = ""):
        if key == "":
            for key in self._settings:
                self._settings[key][-2] = False
        elif key in self._settings:
            self._settings[key][-2] = False
        else:
            print(f'No key "{key}" found in settings')

    def enableComments(self, key = ""):
        if key == "":
            for key in self._settings:
                self._settings[key][-2] = True
        elif key in self._settings:
            self._settings[key][-2] = True
        else:
            print(f'No key "{key}" found in settings')

    def getConfigFile(self):

        IO_paths = ""
        screen_output = ""
        data_details = ""
        dist_freqs_clock = ""
        model_settings = ""
        model_parameters = ""
        branch_optimization = ""
        optional_analysis = ""
        small_diffs = ""

        for key in ["seqfile","outfile","treefile"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    IO_paths += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n"
                else:
                    IO_paths += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        for key in ["noisy","verbose"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    screen_output += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n" 
                else:
                    screen_output += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        for key in ["ndata", "runmode","seqtype","icode","cleandata"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    data_details += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n" 
                else:
                    data_details += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        for key in ["CodonFreq","aaDist","aaRatefile", "clock"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    dist_freqs_clock += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n" 
                else:
                    dist_freqs_clock += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        for key in ["model","NSsites", "ncatG", "Mgene"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    model_settings += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n"        
                else:
                    model_settings += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        for key in ["fix_kappa","kappa","fix_omega","omega","fix_rho","rho"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    model_parameters += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n"      
                else:
                    model_parameters += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        for key in ["fix_blength","method"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    branch_optimization += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n"          
                else:
                    branch_optimization += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        for key in ["getSE","RateAncestor"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    optional_analysis += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n"  
                else:
                    optional_analysis += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"
        
        for key in ["Small_Diff"]:
            if self._settings[key][-1] == True:
                if self._settings[key][-2] == True:
                    small_diffs += f"{self._settings[key][0]}{key} = {self._settings[key][1]}{self._settings[key][2]}\n" 
                else:
                    small_diffs += f"{self._settings[key][0]}{key} = {self._settings[key][1]}\n"

        config_file = f"{IO_paths}\n{screen_output}\n{data_details}\n{dist_freqs_clock}\n{model_settings}\n"\
                f"{model_parameters}\n{branch_optimization}\n{optional_analysis}\n{small_diffs}"

        return config_file

