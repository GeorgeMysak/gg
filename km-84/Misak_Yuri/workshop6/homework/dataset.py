# Vendor,Category, Item, Price, Origin,Destination, Rating, Remarks
# cyberzen,Services/Other,Insider's Forex Trading Signals (Make Thousands of $$$'s DAILY  from my 20 yr Daytrader),2.569571838605444 BTC,,,4.89/5,Average price may be skewed outliar > .5 BTC found

def create_dataset(file):

        dataset = dict()

        with open(file, 'r', encoding="utf8") as f:
            file_line = f.readline()

            if not file_line:
                return dataset

            main_header = file_line.rstrip().split(",")

            file_line = f.readline()
            while file_line:

                [Vendor, Category, Item, Price, Rating,] = [element.strip() for element in file_line.rstrip().split(",")]

                if Vendor not in dataset:
                    dataset[Vendor] = dict()

                if Category not in dataset[Vendor]:
                    dataset[Vendor][Category] = dict()

                dataset[Vendor][Category].update({
                                                Item: {
                                                            'Price': Price,
                                                            'Rating': Rating,

                                                         }
                                            })

                file_line = f.readline()

        return dataset
print(create_dataset('Agora.csv'))