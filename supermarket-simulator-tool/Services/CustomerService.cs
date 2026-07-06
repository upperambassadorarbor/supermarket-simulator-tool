namespace SupermarketSimulatorTool.Services;

public class CustomerService : ICustomerService
{
    private int _total;
    private int _served;

    public int TotalCustomers => _total;
    public int ServedCustomers => _served;

    public void SpawnCustomer()
    {
        Interlocked.Increment(ref _total);
    }

    public void ServeCustomer()
    {
        if (_served < _total)
            Interlocked.Increment(ref _served);
    }
}